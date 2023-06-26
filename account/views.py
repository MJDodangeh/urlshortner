from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User

#Register API
class RegisterApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

