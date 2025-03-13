from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
# Create your views here.

@api_view(["GET"])
def get_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many = True)
    return Response({"ok":True,"tweets":serializer.data})