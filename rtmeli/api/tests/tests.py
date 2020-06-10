import unittest
import re
import requests
import json
from django.test import override_settings
from rtmeli.api.services import MercadolibreApi

class MercadolibreApiTest(unittest.TestCase):

    @override_settings(
        MERCADOLIBRE_CLIENT_ID='3492325516140856', 
        MERCADOLIBRE_CLIENT_SECRET='Bbae1ciMuzxBmRBhh4K7xLJptxWp9zD5'
    )
    def setUp(self):
        self.category = 'MLA420040'
        self.limit = 20
        self.offset = 5
        self.sort = 'price_asc'
        self.user_id = '180370999'
        self.meli = MercadolibreApi(
            limit=self.limit, 
            offset=self.offset, 
            category=self.category, 
            sort=self.sort
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
        self.assertIsInstance(response, list)

    def testGetCategory(self):
        response = self.meli.get_category()
        self.assertIsInstance(response, dict)

    def testGetUserInformation(self):
        response = self.meli.get_user_information(self.user_id)
        self.assertIsInstance(response, dict)