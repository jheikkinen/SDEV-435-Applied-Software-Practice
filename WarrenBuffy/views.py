from django.shortcuts import render, get_object_or_404
from .models.userInfo import userInfo, budgetItems
from .models.forms import budgetItemsForm
from .models.registration import registration, userInfoRegistration


# Create your views here. Pulls html document based on the user's selection.
# Call index html
def index(request):
    users =   userInfo.objects.all()
    return render(request, 'index.html', {'users': users})

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
            profile.save()

            registered = True
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
def budgetManagement(request):
    budgetItem = budgetItems.objects.all()
    return render(request, 'budgetManagement.html', {'budgetItem': budgetItem})


#def budgetManagementEdit(request):
#    return render(request, 'budgetManagementEdit.html')

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
def update_budget_item(request):


    # Retrieve the budget item instance from the database
    budget_item = get_object_or_404(budgetItems)
    
    if request.method == 'POST':
        # If the form is submitted, combine the POST data to the form
        form = budgetItemsForm(request.POST, instance=budget_item)
        if form.is_valid():
            # Save the updated form data to the database
            form.save()
    else:
        # Else keep the remaining items
        form = budgetItemsForm(instance=budget_item)
    
    return render(request, 'budgetManagementEdit.html', {'form': form})