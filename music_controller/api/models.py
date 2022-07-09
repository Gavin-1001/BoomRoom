from django.db import models
import string
import random

def generate_unique_code():
    length = 6
    while(True):
        code = ''.join(random.choices(string.ascii_uppercase, k=6))
        if(Room.objects.filter(code=code)).count() == 0:
            break
        return code 
        ##filter all the rooms to see if the code in the rooms is the same as the code that has been generated.
        ##if not it will return the code, otherwise it will create a new code that is not the same as any of 
        # the codes for the other rooms


# Create your models here.
#
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) # code to accesse the virtual room
    host = models.CharField(max_length=50, unique=True)
    guests_can_pause = models.BooleanField(null=False, default=False) ## does the guest have access to change/pause the song
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True) ##automatically adds date/time of when the room was created
    
    
    