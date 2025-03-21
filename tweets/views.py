from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Tweet
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer
# Create your views here.

class tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TweetSerializer(self,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class tweetsDetail(APIView):
    def get_object(self,pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise Http404
  #      return Response({"ok":True,"tweets":serializer.data})
    
    def get(self,request,pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response({"ok":True,"tweets":serializer.data})

    def put(self,request,pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

