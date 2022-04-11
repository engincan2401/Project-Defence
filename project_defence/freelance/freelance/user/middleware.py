import datetime
from django.utils import timezone
from datetime import timedelta as td
from freelance import settings
from django.utils.deprecation import MiddlewareMixin
from freelance.user.models import CustomUser
from dateutil.parser import parse


class ActiveUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last-activity')

            too_old_time = timezone.now() - td(seconds=settings.LOGIN_INTERVAL)
            if not last_activity or parse(last_activity) < too_old_time:
                CustomUser.objects.filter(pk=request.user.pk).update(
                    last_activity=timezone.now())

            request.session['last-activity'] = timezone.now().isoformat()

        response = self.get_response(request)
        return response
