from django.db import models
from pill.models import Vitamins


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    serial_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)



class VitaminLikes(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    vitamin_id = models.ForeignKey(Vitamins, on_delete=models.CASCADE)


class BuyList(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey

