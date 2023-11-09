# Django
from django.urls import path 

# viewss
from . import views

# Config URL
urlpatterns = [
  path('', views.profile, name='profile'),
]