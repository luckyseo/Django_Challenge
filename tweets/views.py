from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse
# from django.core import serializers
from .models import Tweet, User
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializer import TweetSerializer

from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound


# Create your views here.
def get_tweets(request):
    tweets = Tweet.objects.all()
    return render(request, "show_tweet_list.html", {"tweets": tweets})


class Tweets(APIView):
    # all_tweets = Tweet.objects.all()
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)
