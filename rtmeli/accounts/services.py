from django.conf import settings

from api.services import MercadolibreApi


def get_auth_url():
    meli = MercadolibreApi()
    return meli.get_auth_url()

#TODO: Utilizar metodos de la MercadolibreApi y remover setting
def get_access_token():
    meli = MercadolibreApi()
    if(request.GET.get('code')):
        meli.authorize(request.GET.get('code'), settings.REDIRECT_URL)
    return meli.get_access_token()