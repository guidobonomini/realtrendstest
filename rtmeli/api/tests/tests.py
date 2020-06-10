import unittest
import re
import requests
import json

from api.services import MercadolibreApi

class MercadolibreApiTest(unittest.TestCase):

    def setUp(self):
        self.category = 'MLA420040'
        self.limit = 20
        self.offset = 5
        self.sort = 'price_asc'
        self.meli = MercadolibreApi(
            limit=self.limit, offset=self.offset, category=self.category, sort=self.sort
        )

    #constructor tests
    def testLimit(self):
        self.assertEqual(self.meli.limit, self.limit)

    def testOffset(self):
        self.assertEqual(self.meli.offset, self.offset)

    def testCategory(self):
        self.assertEqual(self.meli.category, self.category)

    def testSort(self):
        self.assertEqual(self.meli.sort, self.sort)

    #requests tests
    def testGetItemsByCategory(self):
        response = self.meli.get_items_by_category()
        self.assertEqual(response.status_code, requests.codes.ok)

    def testGetCategory(self):
        response = self.meli.get_category()
        self.assertEqual(response.status_code, requests.codes.ok)