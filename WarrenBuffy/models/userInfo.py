from django.db import models
from django.contrib.auth.models import User

# Model to pull budget item amounts from database
class budgetItems(models.Model):
    id = models.AutoField(primary_key=True)
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

# Model to pull user information from database
class userInfo(models.Model):
    #username = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=10)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=5)
    authUserId = models.ForeignKey(User, on_delete=models.CASCADE, db_column='authUserId', related_name='auth_user_info')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'userInfo'
        app_label = 'WarrenBuffy'

