import json
from django.conf import settings
from api.services import MercadolibreApi

def get_profile_from_meli(access_token):
    meli = MercadolibreApi(access_token=access_token)
    return meli.get_profile()