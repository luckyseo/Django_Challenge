from django.db import models

# Create your models here.
class Tweet(models.Model):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at=models.DateField()
    updated_at=models.DateField()

    def __str__(self):
        return f"{self.user}'s Tweet"
    
class Like(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE)
    created_at=models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f"{self.user} Liked"