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

    # Verify new passdword is 8 or more characters    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # If new password is less than 8 characters, send error message
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

# Model to take new user information input and store into the database
class userInfoRegistration(forms.ModelForm):

    # Metadata class to identify model and database fields used for form
    class Meta():
        model = userInfo # Work off of userInfo model
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipCode')