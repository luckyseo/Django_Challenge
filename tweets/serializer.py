from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField(max_length=180)
    user_id = serializers.IntegerField()
