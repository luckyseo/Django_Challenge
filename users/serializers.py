from rest_framework import serializers
from .models import User
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"
    #payload = serializers.CharField(source="tweets.payload",read_only=True)

