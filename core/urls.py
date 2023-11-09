from django.urls import path 

# viewss
from . import views

# Config URL
urlpatterns = [
  path('', views.index, name='home'),
]