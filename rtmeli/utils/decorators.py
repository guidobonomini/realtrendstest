import logging

from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger('django')

def login_required():
    def _dec(view_func):
        def _wrapped_view(request, *args, **kwargs):      
            token = request.session.get('access_token', None)
            if not token:
                logger.error('Token not in session', exc_info=True, extra={'request': request.data})
                return HttpResponse('Unauthorized', status=401)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return _dec