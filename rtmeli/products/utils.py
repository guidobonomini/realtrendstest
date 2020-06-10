from collections import defaultdict
from itertools import islice
from threading import Thread

from products.services import get_items_by_category, get_category


def get_top_items_by_price(category_id, limit, sort):
    items = get_items_by_category(category_id, limit=limit, sort=sort)
    return [
        {
            'title':item['title'],
            'price':item['price'],
            'link':item['permalink']
        }
        for item in items]

def get_category_items_count(category_id):
    category = get_category(category_id)
    return category['total_items_in_this_category']

def get_category_items(category_id, total_items, limit=50):
    loops = total_items // limit + (1 if (total_items % limit > 0) else 0)
    items = []
    for i in range(loops):
        offset = limit * i
        items.extend(get_items_by_category(category_id, limit, offset))
    most_sold = find_most_sold(items)
    return most_sold

def find_most_sold(items):
    most_sold = defaultdict(int)
    for item in items:
        most_sold[item['seller']['id']] += item['sold_quantity']
    most_sold = sorted(most_sold.items(), key=lambda items: items[1], reverse=True)
    return most_sold[:10]

