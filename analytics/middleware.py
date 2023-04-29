from django.utils import timezone


class UserVisitMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user and not request.user.is_anonymous:
            visit, created = request.user.uservisit_set.get_or_create(
                defaults={
                    "last_seen": timezone.now(),
                    "visits": 1,
                }
            )

            if not created:
                visit.last_seen = timezone.now()
                visit.visits += 1
                visit.save()

        response = self.get_response(request)
        return response
