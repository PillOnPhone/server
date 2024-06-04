from rest_framework import serializers
from .models import ChattingRooms, Chats, UserChats


class ChattingRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingRooms
        fields = ['user_id', 'pharmacy_id']


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['chatting_room_id', 'content']


class UserChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChats
        fields = ['user_id', 'chat_id']
