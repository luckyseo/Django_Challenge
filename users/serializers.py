from rest_framework import serializers

class UsersSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email =serializers.EmailField()
    #payload = serializers.CharField(source="tweets.payload",read_only=True)

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email =serializers.EmailField()