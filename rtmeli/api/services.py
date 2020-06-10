import json
import requests
from django.conf import settings
from lib.meli import Meli

class MercadolibreApi():
    def __init__(self, *args, **kwargs):
        self.meli = Meli(
            client_id=settings.MERCADOLIBRE_CLIENT_ID, 
            client_secret=settings.MERCADOLIBRE_CLIENT_SECRET, 
            access_token=kwargs.pop('access_token', None),
            refresh_token=kwargs.pop('refresh_token', None)
        )
        self.category = kwargs.pop('category', None)
        self.sort = kwargs.pop('sort','')
        self.limit = kwargs.pop('limit',50)
        self.offset = kwargs.pop('offset',0)
        self.profile_url = self.meli.API_ROOT_URL + 'users/me?access_token='

    def get_category(self):
        response = self.meli.get(path=("/categories/%s" % self.category))
        return json.loads(response.content)

    def get_items_by_category(self):
        params = {
            'category':self.category, 
            'limit':self.limit, 
            'offset':self.offset,
            'sort':self.sort
        }
        response = self.meli.get(path="/sites/MLA/search", params=params)
        return json.loads(response.content)['results']

    def get_auth_url(self):
        return self.meli.auth_url(redirect_URI=settings.REDIRECT_URL)

    def authorize(self, code):
        return self.meli.authorize(code, settings.REDIRECT_URL)

    def get_access_token(self):
        return self.meli.access_token

    def get_profile(self):
        url = self.profile_url
        response = requests.get(
            url,
            params={'access_token': self.access_token},
        )
        return response.content