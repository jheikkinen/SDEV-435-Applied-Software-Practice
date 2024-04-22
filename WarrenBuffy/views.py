from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models.userInfo import userInfo, budgetItems
from .models.forms import budgetItemsForm
from .models.registration import registration, userInfoRegistration
from .models.updateUserInfo import UserContactForm, UserInfoForm, UpdatePassword

# Create your views here. Pulls html document based on the user's selection.
# Call index html
def index(request):
    users =   userInfo.objects.all()
    return render(request, 'index.html', {'users': users})

# Call the index page when user wants to logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Call budget form page html
# Save new user data to database.
def registrationForm(request):
    # Keep false until user successfully registers
    registered = False

    # If the request is POST, save user profile information submitted via form
    if request.method == "POST":
        # Create form instances of the registration and userInfoRegistration class
        register = registration(data=request.POST)
        userRegistration = userInfoRegistration(data=request.POST)

        # If instances are valid, save user profile information, else print errors
        if register.is_valid() and userRegistration.is_valid():

            user = register.save()
            user.set_password(user.password)
            user.save()

            profile = userRegistration.save(commit=False) # Not committing to prevent possible errors
            profile.user = user
            profile.authUserId = user  # Assign the user's ID to the authUserId field
            profile.save()

            # Create a budgetItems instance for the new user with all fields initialized to zero
            budget_items = budgetItems.objects.create(
                user=user,
                income=0,
                mortgage=0,
                utility=0,
                homeMaintenance=0,
                auto=0,
                transportation=0,
                food=0,
                clothing=0,
                entertainment=0,
                childCare=0,
                living=0,
                insurance=0,
                medical=0,
                savings=0,
                debt=0
            )

            registered = True
            return redirect('login')  # Redirect to another page after successful update
        else:
            print(register.errors, userRegistration.errors)

    else:
        # Create blank form instances when user first arrives to page
        register = registration()
        userRegistration = userInfoRegistration()

    return render(request, 'registration.html', 
                  {'register':register, 'userRegistration':userRegistration, 'registered':registered})

# Call home page html
def home(request):
    return render(request, 'home.html')

# Call budget management page html
@login_required
def budgetManagement(request):
    budgetItem = budgetItems.objects.filter(user=request.user)
    return render(request, 'budgetManagement.html', {'budgetItem': budgetItem})

# Call portfolio development and investment tools page html
def pdit(request):
    return render(request, 'PDIT.html')

# Call portfolio growth calculator page html
def portfolioGrowth(request):
    return render(request, 'PortfolioGrowth.html')

# Call investment risk calculator page html
def investmentRisk(request):
    return render(request, 'InvestmentRisk.html')

# Call mortgage calculator page html
def mortgageCalculator(request):
    return render(request, 'mortgageCalculator.html')

# Call budget form page html
# Pull budget item data from the database and save user updated data.
@login_required
def update_budget_item(request):
    # Retrieve the budget item instance for the logged-in user
    budget_item = get_object_or_404(budgetItems, user=request.user)
    
    if request.method == 'POST':
        # If the form is submitted, combine the POST data to the form
        form = budgetItemsForm(request.POST, instance=budget_item)
        if form.is_valid():
            # Save the updated form data to the database
            form.save()
            messages.success(request, 'Budget item updated successfully.')  # Add success message
            return redirect('budgetManagement')  # Redirect to another page after successful update
    else:
        # Else keep the remaining items
        form = budgetItemsForm(instance=budget_item)
    
    return render(request, 'budgetManagementEdit.html', {'form': form})

# Call the user login page
def user_login(request):
    # If the form is submitted, combine the POST data to the form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Verify the username and password are correct
        user = authenticate(username=username,password=password)
        # If user is who they say they are, then log them in, else login failed.
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Login attempt failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'login.html', {})

# Call the profile settings page     
@login_required
def profile_settings(request):
    return render(request, 'profilesettings.html')

# Call the update contact info form
@login_required
def update_contact_info(request):
    if request.method == 'POST':
        user_contact_form = UserContactForm(request.POST, instance=request.user)
        # Get the first userInfo instance related to the current user
        user_info_instance = request.user.user_info.first()
        user_info_form = UserInfoForm(request.POST, instance=user_info_instance)
        if user_contact_form.is_valid() and user_info_form.is_valid():
            user_contact_form.save()
            user_info_form.save()
            return redirect('profilesettings') # Redirect to profile settings if success
    else:
        user_contact_form = UserContactForm(instance=request.user)
        # Get the first userInfo instance related to the current user
        user_info_instance = request.user.user_info.first()
        user_info_form = UserInfoForm(instance=user_info_instance)
    return render(request, 'updatecontactinfo.html', {'user_contact_form': user_contact_form, 'user_info_form': user_info_form })

# Call the update password form
@login_required
def update_user_password(request):
    if request.method == 'POST':
        update_password = UpdatePassword(request.POST)
        if update_password.is_valid():
            old_password = update_password.cleaned_data['old_password']
            new_password = update_password.cleaned_data['new_password']
            confirm_new_password = update_password.cleaned_data['confirm_new_password']

            # Verify if old password is correct
            if not request.user.check_password(old_password):
                messages.error(request, 'Your old password was entered incorrectly, please try again')
                return redirect('passwordchange')
            
            # Verify passwords match
            if new_password != confirm_new_password:
                messages.error(request, 'The passwords did not match')
                return redirect('passwordchange')
            
            # Save the user's new password
            request.user.set_password(new_password)
            request.user.save()

            # Keep the user logged in after the password has been updated
            update_session_auth_hash(request, request.user)

            messages.success(request, 'Your password was successfully updated!')
            return redirect('profilesettings')
    else:
        update_password = UpdatePassword()
    return render(request, 'passwordchange.html', {'update_password': update_password})