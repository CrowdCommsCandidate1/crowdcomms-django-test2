from django.http import Http404

from django.contrib.gis.db.models.functions import Distance

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from foxes.permissions import IsAFox
from foxes.serializers import NearbyRabbitHoleSerializer

from bunnies.models import RabbitHole

# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated & IsAFox])
def get_nearby_active_rabbit_holes(self):
    """
    As a fox, I want to be able to sniff out nearby populated rabbit holes
    Given my current latitude / longitude, return the location name + position + distance of the closest rabbit hole
    that contains at least one rabbit for my dinner, as a lat / lng pair
    """

    queryset = RabbitHole.objects.filter(bunnies__isnull=False).all()

    if not queryset:
        raise Http404

    closest_rabbit_hole = queryset.annotate(
        distance=Distance("location_point", self.user.fox.loocation)
    ).order_by('distance').first()

    ser = NearbyRabbitHoleSerializer(
        instance={
            "location": closest_rabbit_hole.location,
            "distance_km": closest_rabbit_hole.distance.km,
            # TODO: GeoDjango's Azimuth function is not supported by SpatiaLite
            "compass_direction": "N"
        }
    )
    return Response(data=ser.data)
