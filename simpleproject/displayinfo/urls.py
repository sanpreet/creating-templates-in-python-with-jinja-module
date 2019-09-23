from django.urls import path
from . import views

# url route will route to the view provided in the path
urlpatterns=[
path('', views.index, name='index'),
]