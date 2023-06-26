from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import urlShortener
from .serializer import urlShortenerSerializer
import asyncio
import random

class makeUrl(APIView):

    def to_base_62(self,deci):
        s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        hash_str = ''
        while deci > 0:
            hash_str = s[deci % 62] + hash_str
            deci = deci // 62
        return hash_str

    def post(self, request):
        data = request.data
        serializer = urlShortenerSerializer(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.validated_data["user"] = user
            serializer.save()
            obj = urlShortener.objects.get(id=serializer.data["id"])
            shorturl = self.to_base_62((100000000000 + int(obj.id)))
            obj.shorturl = shorturl
            obj.save()
            longurl = data['longurl']
            shorturl = "http://localhost:8000/" + shorturl
            return Response({'longurl': longurl, 'shorturl': shorturl})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class redirectUrl(APIView):
    def get(self, request ,shorturl):
        try:
            obj = urlShortener.objects.get(shorturl=shorturl)
        except urlShortener.DoesNotExist:
            obj = None

        if obj is not None:
            obj.viewcount += 1
            obj.save()
            return redirect(obj.longurl)

class viewCount(APIView):

    def post(self, request):
        data = request.data
        url = data['url']
        try:
            obj = urlShortener.objects.get(shorturl=url)
            return Response({'viewcount': obj.viewcount})
        except urlShortener.DoesNotExist:
            raise Http404

