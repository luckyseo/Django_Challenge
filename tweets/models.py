from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    """Tweet Model Definition"""

    payload = models.CharField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return self.payload

    def like_count(self):
        return self.likes.count()


class Like(CommonModel):
    """Like Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.tweet.payload}"


"""

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

        """
