from rest_framework import generics, status
from rest_framework.response import Response
from .models import ChattingRooms
from .serializers import ChattingRoomsSerializer, ChatsSerializer

from .services import ChattingRoomService


class CreateChattingRoom(generics.CreateAPIView):
    queryset = ChattingRooms.objects.all()
    serializer_class = ChattingRoomsSerializer

    def create(self, request, *args, **kwargs):
        # serializer를 사용하여 데이터 유효성 검사 및 저장 (user, pharmacy 객체 직접 전달)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # POST 요청 데이터에서 user_id, pharmacy_id 값 가져오기
        user_id = request.data.get('user_id')
        pharmacy_id = request.data.get('pharmacy_id')
        content = request.data.get('content')

        # 서비스 계층 함수 호출
        result = ChattingRoomService.create_chattingroom(user_id, pharmacy_id, content)

        # 서비스 계층 함수 결과 처리 (에러 또는 성공 응답)
        if isinstance(result, Response):  # 에러 응답인 경우
            return result
        else:
            chatting_room_serializer, chat_serializer = result
            return Response({
                'success': True,
                'code': 201,
                'message': "요청에 성공하셨습니다.",
                'chatting_room': chatting_room_serializer.data,
                'first_message': chat_serializer.data
            }, status=status.HTTP_201_CREATED)  # 201 Created 상태 코드 반환