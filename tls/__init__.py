from werkzeug.local import Local, release_local


_local = Local()
request = _local('request')


class TLSRequestMiddleware(object):
    def process_request(self, request):
        _local.request = request

    def process_response(self, request, response):
        release_local(_local)
        return response

    def process_exception(self, request, exception):
        release_local(_local)

