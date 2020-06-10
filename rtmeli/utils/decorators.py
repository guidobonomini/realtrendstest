from django.core.exceptions import ObjectDoesNotExist


def login_required():
    def _dec(view_func):
        def _wrapped_view(request, *args, **kwargs):      
            token = request.session.get('access_token', None)
            if not token:
                return HttpResponse('Unauthorized', status=401)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return _dec