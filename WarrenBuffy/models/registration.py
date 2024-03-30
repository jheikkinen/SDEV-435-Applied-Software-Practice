from django import forms
from django.contrib.auth.models import User
from WarrenBuffy.models.userInfo import userInfo

# Model to take new user input and store into the database
class registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    # Metadata class to identify model and database fields used for form
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

# Model to take new user information input and store into the database
class userInfoRegistration(forms.ModelForm):

    # Metadata class to identify model and database fields used for form
    class Meta():
        model = userInfo
        fields = ('phone', 'address1', 'address2', 'city', 'zipCode')