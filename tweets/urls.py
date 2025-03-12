from django.urls import path
from tweets import views

urlpatterns=[
    path("",views.get_Tweets),
]