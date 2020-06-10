import json
from django.conf import settings
from api.services import MercadolibreApi

def get_category_items_count(category_id):
    meli = MercadolibreApi(category=category_id)
    return meli.get_category()['total_items_in_this_category']

def get_items_by_category(category_id, limit=50, offset=0, sort=''):
    meli = MercadolibreApi(category=category_id, limit=limit, offset=offset, sort=sort)
    return meli.get_items_by_category()