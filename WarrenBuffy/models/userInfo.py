from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Model to pull budget item amounts from database
class budgetItems(models.Model):
    # Variables that will serve as columns for the database table.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    income = models.DecimalField(max_digits=15, decimal_places=2)
    mortgage = models.DecimalField(max_digits=15, decimal_places=2)
    utility = models.DecimalField(max_digits=15, decimal_places=2)
    homeMaintenance = models.DecimalField(max_digits=15, decimal_places=2)
    auto = models.DecimalField(max_digits=15, decimal_places=2)
    transportation = models.DecimalField(max_digits=15, decimal_places=2)
    food = models.DecimalField(max_digits=15, decimal_places=2)
    clothing = models.DecimalField(max_digits=15, decimal_places=2)
    entertainment = models.DecimalField(max_digits=15, decimal_places=2)
    childCare = models.DecimalField(max_digits=15, decimal_places=2)
    living = models.DecimalField(max_digits=15, decimal_places=2)
    insurance = models.DecimalField(max_digits=15, decimal_places=2)
    medical = models.DecimalField(max_digits=15, decimal_places=2)
    savings = models.DecimalField(max_digits=15, decimal_places=2)
    debt = models.DecimalField(max_digits=15, decimal_places=2)


    class Meta:
        db_table = 'budgetItems'
        app_label = 'WarrenBuffy'

    # Get budget surplus or deficit
    def total(self):
        # Add every expense
        total_sum = sum([self.mortgage, self.utility, self.homeMaintenance, self.auto,
                    self.transportation, self.food, self.clothing, self.entertainment, self.childCare,
                    self.living, self.insurance, self.medical, self.savings, self.debt])
                
        # Multiply monthly expenses to get annual expense
        total_expenses = total_sum * 12  

        # Income - Expenses to get surplus or deficit
        total = self.income - total_expenses
        return total

# Model to pull user information from database
class userInfo(models.Model):
    # Variables that will serve as columns for the database table.
    phone = models.CharField(max_length=10)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=5)
    authUserId = models.ForeignKey(User, on_delete=models.CASCADE, db_column='authUserId', related_name='user_info', default=None, null=True)

    # Verify Zipcode is an actual number.
    def clean(self):
        super().clean()
        # If zipCode not a number return error message
        if not self.zipCode.isdigit():
            raise ValidationError({'zipCode': 'Zip code must contain only numeric digits.'})

    def __str__(self):
        return self.authUserId.username

    class Meta:
        db_table = 'userInfo'
        app_label = 'WarrenBuffy'