from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def get_all_tweets(request, pk):
    user = User.objects.filter(pk=pk) #this is not json -> can't be displayed -> need serializer
    serializer = serializers.serialize("json",user)
    return JsonResponse({"user":serializer})