from django.db import models
from pharmacy.models import Pharmacy


class Vitamins(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=20, null=True)
    ingredient = models.CharField(max_length=50, null=True, default="")
    performance = models.CharField(max_length=200, null=True)
    warningnotice = models.CharField(max_length=200, null=True)
    takingtimes = models.CharField(max_length=20, null=True)


class PharmacyVitamins(models.Model):
    id = models.AutoField(primary_key=True)
    vitamin_id = models.ForeignKey(Vitamins, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

