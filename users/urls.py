from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path("<int:pk>/tweets",views.get_all_tweets)
]