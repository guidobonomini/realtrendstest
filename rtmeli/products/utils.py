from collections import defaultdict
from threading import Thread

def find_most_sold(items, range):
    #adds the sold_quantity for a users sold items and sorts it by top sellers
    most_sold = defaultdict(int)
    for item in items:
        most_sold[item['seller']['id']] += item['sold_quantity']
    most_sold = sorted(most_sold.items(), key=lambda items: items[1], reverse=True)
    return most_sold[:range]

def rearrange_dictionary(items):
    #creates a list of dictionaries for the sellers
    return [{'id': item[0],'position': idx} for idx, item in enumerate(items)]

## TODO: Unify process_threads and process_threads_users since they perform a similar task
def process_threads(function, **params):
    #process parallel threads for calling Mercadolibre api without mayor delay
    items = []
    threads = []
    for i in range(params.get('nthreads',1)):
        offset = params.get('limit',50) * i
        t = Thread(target=function, args=(
            params.get('category'),
            params.get('limit'),
            offset,
            items
            )
        )
        threads.append(t)
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]
    return items

def process_threads_users(function, users):
    #process parallel threads for calling Mercadolibre api without mayor delay
    items = [0]*len(users)
    threads = []
    for i in range(len(users)):
        t = Thread(target=function, args=(
            users[i],
            items
            )
        )
        threads.append(t)
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]
    return items