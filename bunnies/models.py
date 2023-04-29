from django.conf import settings
from django.db import models

# Create your models here.


class RabbitHole(models.Model):
    '''
    Rabbits live in rabbit holes
    '''
    location = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bunnies_limit = models.PositiveIntegerField(default=5)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    @property
    def bunny_count(self):
        return self.bunnies.count()

    def __str__(self) -> str:
        return self.location


class Bunny(models.Model):
    '''
    The rabbits
    '''
    name = models.CharField(max_length=64)
    home = models.ForeignKey(RabbitHole, on_delete=models.CASCADE, related_name='bunnies')

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"
