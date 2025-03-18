from django.shortcuts import render
from .models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import UsersSerializer
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
# Create your views here.

class Users(APIView):
    def get(self,request):
        try:
            user = User.objects.all() #this is not json -> can't be displayed -> need serializer
            serializer = UsersSerializer(user,many=True)
            return Response({"ok":True,"user":serializer.data})
        except User.DoesNotExist:
            raise NotFound("No User")
    # user_tweets = user.tweets.all()

class UsersDetails(APIView):
    def get(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UsersSerializer(user)
            return Response({"user":serializer.data})
        except User.DoesNotExist:
            raise NotFound(f"no id:{pk} user")
    
class Tweets(APIView):
    def get(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
            tweets=user.tweets.all()
            serialzer = TweetSerializer(tweets,many=True)
            return Response({"ok":True,"tweets":serialzer.data})
        except:
            raise NotFound("404")