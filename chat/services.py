from .models import ChattingRooms, Chats, UserChats, PharmacyChats
from user.models import Users
from pharmacy.models import Pharmacy
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import ChattingRoomsSerializer, ChatsSerializer


class ChattingRoomService:
    @staticmethod
    def create_chattingroom(user_id, pharmacy_id, content):

        try:
            # user_id와 pharmacy_id를 사용하여 User 및 Pharmacy 객체 가져오기
            user = Users.objects.get(pk=user_id)
            pharmacy = Pharmacy.objects.get(pk=pharmacy_id)
        except (Users.DoesNotExist, Pharmacy.DoesNotExist):
            return Response({
                'success': False,
                'code': 400,
                'error': 'Invalid user_id or pharmacy_id.',
            }, status=status.HTTP_400_BAD_REQUEST)

        # 기존 채팅방 존재 여부 확인
        existing_chatting_room = ChattingRooms.objects.filter(user_id=user_id, pharmacy_id=pharmacy_id).first()
        if existing_chatting_room:
            return Response({
                'success': False,
                'code': 400,
                'error': 'Chatting room already exists.',
            }, status=status.HTTP_400_BAD_REQUEST)

        chatting_room = ChattingRooms.objects.create(user_id=user, pharmacy_id=pharmacy)

        # 첫 번째 메시지(관심 약) 생성
        chat = Chats.objects.create(chatting_room_id=chatting_room, content=content)

        # UserChats에 기록
        UserChats.objects.create(user_id=chatting_room.user_id, chat_id=chat)

        # 생성된 채팅방 정보와 첫 메시지 정보를 함께 반환
        chatting_room_serializer = ChattingRoomsSerializer(chatting_room)
        chat_serializer = ChatsSerializer(chat)

        # PharmacyChats에 기록
        #PharmacyChats.objects.create(pharmacy_id=chatting_room.pharmacy_id, chat_id=chat)

        return chatting_room_serializer, chat_serializer