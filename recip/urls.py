from django.urls import path
from recip.views import home

urlpatterns = [
    path('home', home, name='home'),


]