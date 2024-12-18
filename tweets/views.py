from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


# Create your views here.
def get_tweets(request):
    tweets = Tweet.objects.all()
    return render(request, "show_tweet_list.html", {"tweets": tweets})
