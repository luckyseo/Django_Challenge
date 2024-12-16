from django.db import models
from common.models import CommonModel


# Create your models here.
class Tweet(CommonModel):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user}'s Tweet"

    def count_like(self):
        return self.likes.count()


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.user} Liked"
