from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweets),
    path("", views.Tweets.as_view()),
]
