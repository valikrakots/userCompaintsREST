
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import CustomUserSerializer

from .tasks import send_email_task


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = None
            try:
                user = serializer.save()
            except:
                return Response("The user is allready registered", status=status.HTTP_403_FORBIDDEN)
            send_email_task.delay(request.data.get("email"))
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



