from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweets),
    path("api/v1/tweets", views.list_all_tweets, name="list_all_tweets"),
    path("api/v1/users/<int:user_id>/tweets", views.user_tweets, name="user_tweets"),
]
