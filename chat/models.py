from django.db import models
from pharmacy.models import Pharmacy
from user.models import Users


class ChattingRooms(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    is_started = models.BooleanField(default=False)


class Chats(models.Model):
    id = models.AutoField(primary_key=True)
    chatting_room_id = models.ForeignKey(ChattingRooms, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    time = models.DateTimeField(auto_now_add=True)


class PharmacyChats(models.Model):
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chats, on_delete=models.CASCADE)


class UserChats(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chats, on_delete=models.CASCADE)
