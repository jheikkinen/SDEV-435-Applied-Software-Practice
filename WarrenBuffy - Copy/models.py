from django.db import models

class MyModel(models.Model):
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
        app_label = 'WarrenBuffy'