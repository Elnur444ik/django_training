import time


class RequestDelay:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        self.count += 1

        if self.count % 5 == 0:
            time.sleep(5)

        response = self.get_response(request)

        return response
