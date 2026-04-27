from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
  
    def __str__(self):
        return f"{self.city} ({self.name})"

class Route(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()
  
    passengers = models.ManyToManyField(User, blank=True, related_name='routes')
  
    def __str__(self):
        return f"{self.origin} to {self.destination}"