##Responsible for returning code in models.py into JSON for the frontend to read 
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guests_can_pause', 'votes_to_skip', 'created_at') ##if for primary key in db