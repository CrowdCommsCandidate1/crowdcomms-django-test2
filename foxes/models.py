from django.db import models
from django.conf import settings

from django.contrib.gis.geos import GEOSGeometry, Point


class Fox(models.Model):
    name = models.CharField(max_length=32)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    @property
    def loocation(self):
        return GEOSGeometry(Point(self.latitude, self.longitude), srid=4326)
