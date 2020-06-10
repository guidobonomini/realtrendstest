from django.shortcuts import render
from django.views.generic import TemplateView

from products.utils import (
    get_category_items, get_category_items_count, 
    get_top_items_by_price
)

class TopSellersView(TemplateView):
    def get(self,request):
        category_id = "MLA420040"
        total_items_category = get_category_items_count(category_id)
        items_list = get_category_items(category_id, total_items_category)
        return render(request,'pages/topsellers.html',{'items':items_list})

top_sellers_view = TopSellersView.as_view()

class TopPriceItemsView(TemplateView):
    def get(self,request):
        category_id = "MLA420040"
        limit = 10
        sort = 'price_desc'
        items_list = get_top_items_by_price(category_id, limit, sort)
        return render(request,'pages/topprices.html',{'items':items_list})

top_prices_view = TopPriceItemsView.as_view()