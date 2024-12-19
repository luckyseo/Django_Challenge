from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse
# from django.core import serializers
from .models import Tweet, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializer import TweetSerializer


# Create your views here.
def get_tweets(request):
    tweets = Tweet.objects.all()
    return render(request, "show_tweet_list.html", {"tweets": tweets})


@api_view(["GET"])
def db_tweets(request):
    # all_tweets = Tweet.objects.all()
    all_tweets = Tweet.objects.all()
    serializer = TweetSerializer(all_tweets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def user_generated_Tweets(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound("User Not Found")

    user_generated_tweets = user.tweets.all()  # Access user's tweets via related_name
    serializer = TweetSerializer(user_generated_tweets, many=True)
    return Response(serializer.data)
