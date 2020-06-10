import sys
import json
sys.path.append('../../lib')
from django.conf import settings
from meli import Meli

meli = Meli(client_id=settings.MERCADOLIBRE_CLIENT_ID, client_secret=settings.MERCADOLIBRE_CLIENT_SECRET)

def get_category(category_id):
    response = meli.get(path=("/categories/%s" % category_id))
    return json.loads(response.content)

def get_items_by_category(category_id, limit=50, offset=0, sort=''):
    params = {
        'category':category_id, 
        'limit':limit, 
        'offset':offset,
        'sort':sort
    }
    response = meli.get(path="/sites/MLA/search", params=params)
    return json.loads(response.content)['results']