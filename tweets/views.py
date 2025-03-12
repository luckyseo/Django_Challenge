from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
# Create your views here.


def get_Tweets(request):
    tweets = Tweet.objects.all()
    return render(request,"all_tweets.html",{"tweets":tweets})