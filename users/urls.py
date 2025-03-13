from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path("",views.get_all_users),
    path("<int:pk>",views.get_user),
    path("<int:pk>/tweets",views.get_user_tweets)
]