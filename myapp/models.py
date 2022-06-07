from django.db import models


# Create your models here.
class Company(models.Model):
    """Company model"""
    companyName = models.CharField(max_length=255, null=False) # Company name
    ricCode = models.CharField(max_length=255, null=False) # Code

    def __str__(self):
        """Returns a string representation of the model"""
        return self.companyName
