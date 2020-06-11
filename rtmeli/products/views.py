from django.shortcuts import render
from django.views.generic import TemplateView

from .services import (
    get_category_items_count,
    get_most_sold_seller_ids,
    get_top_items_by_price,
    get_users_nicknames
)

class TopSellersView(TemplateView):
    def get(self,request):
        category_id = "MLA420040"
        if (request.session.get('access_token',None)):
            token = request.session['access_token']
        total_items_category = get_category_items_count(category_id)
        seller_ids = get_most_sold_seller_ids(category_id, total_items_category)
        sellers = get_users_nicknames(seller_ids)
        return render(request,'pages/topsellers.html',{'items':sellers})

top_sellers_view = TopSellersView.as_view()

class TopPriceItemsView(TemplateView):
    def get(self,request):
        category_id = "MLA420040"
        limit = 10
        sort = 'price_desc'
        items_list = get_top_items_by_price(category_id, limit, sort)
        return render(request,'pages/topprices.html',{'items':items_list})

top_prices_view = TopPriceItemsView.as_view()