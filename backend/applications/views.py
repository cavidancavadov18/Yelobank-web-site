from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.serializers import ApplicationSerializer, QueueTicketSerializer


class ApplicationCreateView(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"ok": True}, status=status.HTTP_201_CREATED)


class QueueCreateView(APIView):
    def post(self, request):
        serializer = QueueTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        return Response({"ok": True, "code": ticket.code}, status=status.HTTP_201_CREATED)
