from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user  

class Counter(models.Model):
    counter_id = models.IntegerField(primary_key=True, unique=True)
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.counter_id
    
class Table(models.Model):
    table_id = models.IntegerField(primary_key=True, unique=True)
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.table_id
    
class TatamiRoom(models.Model):
    tatami_room_id = models.IntegerField(primary_key=True, unique=True)
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tatami_room_id
    
class KaraokeRoom(models.Model):
    karaoke_room_id = models.IntegerField(primary_key=True, unique=True)
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.karaoke_room_id