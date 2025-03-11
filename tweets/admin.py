from django.contrib import admin
from .models import Tweet, Like
# Register your models here.
class detectElonMusk(admin.SimpleListFilter):
    title = "Filter the Elon Musk"
    parameter_name="ElonMusk"

    def lookups(self, request, TweetAdmin):
        return [
            ("ElonMusk","Elon Musk"),

        ]
    def queryset(self, request, tweets):
        url = self.value() #reat URL instead of request.GET
        if url:
            if url == "ElonMusk":
                return tweets.filter(user__username__contains = url)
            else: 
                return tweets.filter(user__username__icontains=url)
        else:
            tweets

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display=("payload","like_count")
    list_filter=(detectElonMusk,"created_at",)
    search_fields=(
        "payload","user_username",
    )
    def like_count(self, tweet):
        return tweet.likes.count()
    


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields=("user__username",)
    list_display=("tweet","user")
    list_filter=("created_at",)
    