from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import TweetSerializer
# Create your views here.

class tweets(APIView):
    def get_objects(request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many = True)
        return Response({"ok":True,"tweets":serializer.data})