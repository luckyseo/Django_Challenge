from django.urls import path
from tweets import views

urlpatterns=[
    path("",views.tweets.as_view()),
]