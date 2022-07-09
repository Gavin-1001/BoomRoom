from django.urls import path
from .views import main

urlpatterns = [
    path('home', main) 
    ##If this has a blank url, should send you to localhost:8000/ and it will call the function named main defined in api/views
]