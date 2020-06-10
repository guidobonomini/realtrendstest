import unittest
import re
import requests
import json
from django.test import override_settings

from ..services import (
    get_most_sold_seller_ids,
    get_category_items_count,
    get_top_items_by_price,
    get_users_nicknames
)

class ProductsTest(unittest.TestCase):

    def setUp(self):
        self.category = 'MLA420040'
        self.limit = 20
        self.offset = 5
        self.sort = 'price_asc'
        self.total_items = 500
        self.users = ['180370999', '180370100']

    #requests tests
    @override_settings(
        MERCADOLIBRE_CLIENT_ID='3492325516140856', 
        MERCADOLIBRE_CLIENT_SECRET='Bbae1ciMuzxBmRBhh4K7xLJptxWp9zD5'
    )
    def testGetItemsByCategory(self):
        response = get_most_sold_seller_ids(
            category_id=self.category, 
            total_items=self.total_items, 
            limit=self.limit, 
            offset=self.offset
        )
        self.assertIsNotNone(response)

    @override_settings(
        MERCADOLIBRE_CLIENT_ID='3492325516140856', 
        MERCADOLIBRE_CLIENT_SECRET='Bbae1ciMuzxBmRBhh4K7xLJptxWp9zD5'
    )  
    def testGetCategoryItemsCount(self):
        response = get_category_items_count(self.category)
        self.assertIsInstance(response, int)

    @override_settings(
        MERCADOLIBRE_CLIENT_ID='3492325516140856', 
        MERCADOLIBRE_CLIENT_SECRET='Bbae1ciMuzxBmRBhh4K7xLJptxWp9zD5'
    )
    def testGetTopItemsByPrice(self):
        response = get_top_items_by_price(
            category_id=self.category,
            limit=self.limit, 
            sort=self.sort
        )
        self.assertIsNotNone(response)

    @override_settings(
        MERCADOLIBRE_CLIENT_ID='3492325516140856', 
        MERCADOLIBRE_CLIENT_SECRET='Bbae1ciMuzxBmRBhh4K7xLJptxWp9zD5'
    )
    def testGetUsersNicknames(self):
        response = get_users_nicknames(self.users)
        self.assertIsNotNone(response)