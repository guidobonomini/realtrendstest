import json
from django.conf import settings

from products.utils import find_most_sold, process_threads, rearrange_dictionary, process_threads_users
from api.services import MercadolibreApi

def get_category_items_count(category_id):
    #gets the total items in a category
    meli = MercadolibreApi(category=category_id)
    return meli.get_category()['total_items_in_this_category']

def get_top_items_by_price(category_id, limit=50, sort=''):
    #gets the top priced items in a category
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
    #gets the best sellers ids in a category
    nthreads = total_items // limit + (1 if (total_items % limit > 0) else 0)
    items = process_threads(
        process_request, category=category_id, 
        total_items=total_items, limit=limit, nthreads=nthreads
    )
    most_sold = find_most_sold(items, 10)
    sellers_ids = rearrange_dictionary(most_sold)
    print(sellers_ids)
    return sellers_ids

def get_user_nickname(users):
    #gets the users nicknames by id
    meli = MercadolibreApi()
    items = process_threads_users(
        process_request_users, users=users
    )
    return items

# TODO: Unify both methods since they do similar tasks

def process_request(category, limit, offset, items):
    #process Meli api calls and adds the results to an array
    meli = MercadolibreApi(category=category, limit=limit, offset=offset)
    items.extend(meli.get_items_by_category())
    return items

def process_request_users(user, items):
    #process Meli api calls and assigns the results to an array
    meli = MercadolibreApi()
    items[user['position']] = (meli.get_user_information(user['id']))
    return items
