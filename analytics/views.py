from datetime import datetime

from django.utils import timezone
from django.db.models import Sum

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.models import UserVisit


class HelloWorld(APIView):
    """
    Basic 'Hello World' view. Show our current API version, the current time, the number of recent visitors
    in the last 1 hour, and the total number of visitors and page visits
    """

    def get(self, request, format=None):
        valid_visitors = UserVisit.objects.filter(
            visits__gte=1,
        )

        recent_visitors = valid_visitors.filter(
            last_seen__gt=timezone.now() - timezone.timedelta(hours=1)
        )

        all_visits = recent_visitors.aggregate(Sum("visits"))

        data = {
            'version': 1.0,
            'time': timezone.now(),
            'recent_visitors': recent_visitors.count(),
            'all_visitors': valid_visitors.count(),
            'all_visits': all_visits.get("visits__sum"),
        }
        return Response(data)

