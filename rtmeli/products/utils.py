from collections import defaultdict
from itertools import islice
from threading import Thread

from products.services import get_items_by_category


def get_top_items_by_price(category_id, limit, sort):
    items = get_items_by_category(category_id, limit=limit, sort=sort)
    return [
        {
            'title':item['title'],
            'price':item['price'],
            'link':item['permalink']
        }
        for item in items]

def process_request(category_id, limit, offset, items):
    items.extend(get_items_by_category(category_id, limit, offset))
    return items

def get_category_items(category_id, total_items, limit=50):
    nthreads = total_items // limit + (1 if (total_items % limit > 0) else 0)
    items = []
    threads = []
    for i in range(nthreads):
        offset = limit * i
        t = Thread(target=process_request, args=(category_id, limit, offset, items))
        threads.append(t)
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]
    most_sold = find_most_sold(items)
    return most_sold

def find_most_sold(items):
    most_sold = defaultdict(int)
    for item in items:
        most_sold[item['seller']['id']] += item['sold_quantity']
    most_sold = sorted(most_sold.items(), key=lambda items: items[1], reverse=True)
    return most_sold[:10]

