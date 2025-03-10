from django.contrib import admin
from .models import Tweet, Like
# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display=("payload","like_count")
    def like_count(self, tweet):
        return tweet.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=("tweet","user")