from django.db import models


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

