from django.urls import path

from rtmeli.products.views import (
    top_prices_view,
    top_sellers_view,
)

app_name = "products"
urlpatterns = [
    path("top_prices/", view=top_prices_view, name="top_prices"),
    path("top_sellers/", view=top_sellers_view, name="top_sellers"),
]
