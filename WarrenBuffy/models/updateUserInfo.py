from django import forms
from django.contrib.auth.models import User
from .userInfo import userInfo
from django.core.exceptions import ValidationError

# Form used to update the user profile information.
class UserContactForm(forms.ModelForm):
    class Meta:
        model = User # Work off of Django User model
        fields = ('first_name', 'last_name', 'email')
        # Used to label the fields of the form
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',            
        }

class UserInfoForm(forms.ModelForm):
    # Verify Zipcode is an actual number.
    def clean_zipCode(self):
        zipCode = self.cleaned_data.get('zipCode')
        # If zipCode not a number return error message
        if not zipCode.isdigit():
            raise ValidationError('Zip code must contain only numeric digits.')
        return zipCode
        
    class Meta:
        model = userInfo # Work off of userInfo model
        fields = ['phone', 'address1', 'address2', 'city', 'state', 'zipCode']
        # Used to label the fields of the form
        labels = {
            'phone': 'Phone',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'city': 'City',
            'state': 'State',
            'zipCode' : 'Zip Code',
        }

# Class to update the user's password
class UpdatePassword(forms.Form):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput)
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    # Verify new passdword is 8 or more characters
    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        # If new password is less than 8 characters, send error message
        if len(new_password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return new_password