from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweets),
    path("api/v1/tweets", views.db_tweets, name="db_tweets"),
    path(
        "api/v1/users/<int:user_id>/tweets",
        views.user_generated_Tweets,
        name="user_generated_Tweets",
    ),
]
