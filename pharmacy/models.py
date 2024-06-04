from django.db import models
from user.models import Users
from pill.models import Vitamins

class Pharmacy(models.Model):
    """
    약국 정보를 저장하는 모델
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=50)
    serial_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_noticed = models.BooleanField(default=False)


class Pharmacist(models.Model):
    """
    약사 정보를 저장하는 모델
    """
    id = models.AutoField(primary_key=True)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

class Pharmacy_Review(models.Model):
    """
    약국 리뷰 정보에 대한 모델
    """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    content = models.CharField(max_length=50, null=True)

class PharmacyLikes(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PharmacyVitamins(models.Model):
    id = models.AutoField(primary_key=True)
    vitamin_id = models.ForeignKey(Vitamins, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
