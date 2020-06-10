import unittest
import re
import requests
import json

from products.services import (
    get_category_items,
    get_category_items_count,
    get_top_items_by_price
)

class ProductsiTest(unittest.TestCase):

    def setUp(self):
        self.category = 'MLA420040'
        self.limit = 20
        self.offset = 5
        self.sort = 'price_asc'
        self.total_items = 500

    #requests tests
    def testGetItemsByCategory(self):
        response = self.get_category_items(
            category_id=self.category, 
            total_items=self.total_items, 
            limit=self.limit, 
            offset=self.offset
        )
        self.assertIsNotNone(response)
        
    def testGetCategoryItemsCount(self):
        response = self.get_category_items_count(self.category)
        self.assertIsInstance(response, int)

    def testGetTopItemsByPrice(self):
        response = self.get_top_items_by_price(
            category_id=self.category,
            limit=self.limit, 
            sort=self.sort
        )
        self.assertIsNotNone(response)