from django.db import models
from users.models import User

# Create your models here.

# This is abstract class to save Date & Time
class Generated_DateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add sets time when it is created
    updated_at = models.DateTimeField(auto_now=True) #auto_now updates field when it is updated

    class Meta:
        abstract = True

class Tweet(Generated_DateTime):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return "@{self.user.username} tweeted {self.payload}"

class Like(Generated_DateTime):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        Tweet, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "@{self.user.username} liked tweet {self.tweet}"