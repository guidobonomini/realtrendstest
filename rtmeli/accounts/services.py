from api.services import MercadolibreApi

def get_auth_url():
    meli = MercadolibreApi()
    return meli.get_auth_url()

def authorize(code):
    meli = MercadolibreApi()
    return meli.authorize(code)

def get_access_token():
    meli = MercadolibreApi()
    return meli.get_access_token()