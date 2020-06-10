import json
import sys
sys.path.append('../lib')
from django.conf import settings
from lib.meli import Meli

meli = Meli(client_id=settings.MERCADOLIBRE_CLIENT_ID, client_secret=settings.MERCADOLIBRE_CLIENT_SECRET)

def get_auth_url():
    return meli.auth_url(redirect_URI=settings.REDIRECT_URL)

def authorize(code):
    return meli.authorize(code, settings.REDIRECT_URL)

def get_access_token():
    return meli.access_token