import json
from django.conf import settings

from products.utils import find_most_sold, process_threads, rearrange_dictionary
from api.services import MercadolibreApi

def get_category_items_count(category_id):
    meli = MercadolibreApi(category=category_id)
    return meli.get_category()['total_items_in_this_category']

def get_top_items_by_price(category_id, limit=50, sort=''):
    meli = MercadolibreApi(category=category_id, limit=limit, sort=sort)
    items = meli.get_items_by_category()
    return [
        {
            'title':item['title'],
            'price':item['price'],
            'link':item['permalink']
        }
        for item in items]

def get_most_sold_seller_ids(category_id, total_items, limit=50, offset=0):
    nthreads = total_items // limit + (1 if (total_items % limit > 0) else 0)
    items = process_threads(
        process_request, category=category_id, 
        total_items=total_items, limit=limit, nthreads=nthreads
    )
    most_sold = find_most_sold(items, 10)
    print(most_sold)
    sellers_ids = rearrange_dictionary(most_sold)
    return sellers_ids

def get_user_nickname(users):
    meli = MercadolibreApi()
    return [meli.get_user_information(user) for user in users]

def process_request(category, limit, offset, items):
    meli = MercadolibreApi(category=category, limit=limit, offset=offset)
    items.extend(meli.get_items_by_category())
    return items
