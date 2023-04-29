from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from bunnies.models import Bunny, RabbitHole
from bunnies.permissions import RabbitHolePermissions
from bunnies.serializers import BunnySerializer, RabbitHoleSerializer


class RabbitHoleViewSet(viewsets.ModelViewSet):
    serializer_class = RabbitHoleSerializer
    permission_classes = (IsAuthenticated, RabbitHolePermissions)
    queryset = RabbitHole.objects.all()

    def filter_queryset(self, queryset):
        # Limiting full queryset for superusers to DELETE operations
        if self.request.user.is_superuser and self.action == "destroy":
            return queryset
        return queryset.filter(owner=self.request.user)


class BunnyViewSet(viewsets.ModelViewSet):
    serializer_class = BunnySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Bunny.objects.all()