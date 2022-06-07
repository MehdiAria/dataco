from django.db import models


# Create your models here.
class Company(models.Model):
    companyName = models.CharField(max_length=255, null=False)
    ricCode = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.companyName
