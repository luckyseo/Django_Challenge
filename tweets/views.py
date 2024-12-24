from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse
# from django.core import serializers
from .models import Tweet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializer import TweetSerializer

from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound


# Create your views here.
class Tweets(APIView):
    # all_tweets = Tweet.objects.all()
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save()
            return Response(TweetSerializer(tweet).data)
        else:
            return Response(serializer.errors)


class TweetsDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        return Response(
            TweetSerializer(
                self.get_object(pk),
            ).data,
        )

    def put(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(
                TweetSerializer(updated_tweet).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
