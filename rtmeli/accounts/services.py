from api.services import MercadolibreApi


def get_auth_url():
    meli = MercadolibreApi()
    return meli.get_auth_url()

#TODO: Utilizar metodos de la MercadolibreApi y remover setting
def get_access_token(code):
    meli = MercadolibreApi()
    meli.authorize(code)
    return meli.get_access_token()