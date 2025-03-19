from django.shortcuts import render
from django.contrib.auth import authenticate , login, logout
from .models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import UsersSerializer
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
"""
GET /api/v1/users: See all users [x]
POST /api/v1/users: Create a user account with password - pk error
PUT /api/v1/users/password: Edit logged in user password [x]
POST /api/v1/users/login: Log a user in [x]
POST /api/v1/users/logout: Log a user out [x]
"""
class Users(APIView):
   # permission_classes=[IsAuthenticated] #only for logged-in User

    def get(self,request):
        try:
            user = User.objects.all() #this is not json -> can't be displayed -> need serializer
            serializer = UsersSerializer(user,many=True)
            return Response({"ok":True,"user":serializer.data})
        except User.DoesNotExist:
            raise NotFound("No User")
    # user_tweets = user.tweets.all()

    #Create a user account with password
    def post(self,request):
        pw= request.data.get('password')
        if not pw:
            raise ParseError
        serializer=UsersSerializer(self,data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(pw) #hasging by django
            user.save()
            serializer = UsersSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        """
        {
            "username": "testuser1",
            "first_name": "test",
            "last_name": "user1",
            "password":"12345"
        }
        """
    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        return user
    
class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request):
        user=request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
             raise ParseError
        if user.check_password(old_password):
             user.set_password(new_password)
             user.save()
             return Response(status=status.HTTP_200_OK)
        else:
             raise ParseError
        """
        {"old_password":"1234","new_password":"123"}
        """
class LogIn(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return Response({"ok":"welcome"})
        else:
            return Response({"error":"wrongPassword"})

class LogOut(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({"ok":"bye"})

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
        