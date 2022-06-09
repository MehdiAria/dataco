from django.db import models


class Company(models.Model):
    """Company model"""
    companyName = models.CharField(max_length=255, null=False)  # Company name
    ricCode = models.CharField(max_length=255, null=False)  # Code

    def __str__(self):
        """Returns a string representation of the model"""
        return self.companyName


class Esg(models.Model):
    """Company model"""
    esg = models.CharField(max_length=5, null=False)
    environment = models.CharField(max_length=5, null=False)
    social = models.CharField(max_length=5, null=False)
    governance = models.CharField(max_length=5, null=False)
    rank = models.CharField(max_length=5, null=False)
    total = models.CharField(max_length=5, null=False)
    ricCode = models.CharField(max_length=5, null=False)

    def __str__(self):
        """Returns a string representation of the model"""
        return self.ricCode
