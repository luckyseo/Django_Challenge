from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField(max_length=180)
    username = serializers.CharField(source="user.username", read_only=True)
