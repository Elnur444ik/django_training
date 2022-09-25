from django.core.cache import cache
from django.core.exceptions import PermissionDenied


class RequestLimit:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        count = cache.get_or_set(f'ip:{ip}', 0, 10)
        count += 1
        if count > 3:
            raise PermissionDenied
        else:
            cache.set(f'ip:{ip}', count, 10)

        response = self.get_response(request)

        return response
