import json
import requests
from django.conf import settings
from ..lib.meli_sdk.meli import Meli

class MercadolibreApi():
    def __init__(self, *args, **kwargs):
        self.meli = Meli(
            client_id=kwargs.get('client_id', settings.MERCADOLIBRE_CLIENT_ID),
            client_secret=kwargs.get('client_secret', settings.MERCADOLIBRE_CLIENT_SECRET), 
            access_token=kwargs.get('access_token', None),
            refresh_token=kwargs.get('refresh_token', None)
        )
        self.category = kwargs.get('category', None)
        self.sort = kwargs.get('sort','')
        self.limit = kwargs.get('limit',50)
        self.offset = kwargs.get('offset',0)
        self.profile_url = self.meli.API_ROOT_URL + '/users/me'

    def get_category(self):
        #gets a specific category information
        response = self.meli.get(path=("/categories/%s" % self.category))
        return json.loads(response.content)

    def get_items_by_category(self):
        #gets items by an specified id
        params = {
            'category':self.category, 
            'limit':self.limit, 
            'offset':self.offset,
            'sort':self.sort
        }
        response = self.meli.get(path="/sites/MLA/search", params=params)
        return json.loads(response.content)['results']

    def get_user_information(self, user_id):
        #gets user information by an specified user id
        response = self.meli.get(path=("/users/%s" % user_id))
        return json.loads(response.content)

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
            params={'access_token': self.meli.access_token},
        )
        return response.content