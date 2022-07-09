from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

#All end points are written here
# Create your views here.

#Api View

class RoomView(generics.ListAPIView):
    ##allows user to view and create a room
    ##created view that will return all the rooms created and allow the user to create a room
    queryset = Room.objects.all() ## queryset = what we want to return in this case all of the room objects
    serializer_class = RoomSerializer ## 
    
    
    