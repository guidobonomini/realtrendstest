from collections import defaultdict
from threading import Thread

def find_most_sold(items, range):
    most_sold = defaultdict(int)
    for item in items:
        most_sold[item['seller']['id']] += item['sold_quantity']
    most_sold = sorted(most_sold.items(), key=lambda items: items[1], reverse=True)
    return most_sold[:range]

def process_threads(function, **params):
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