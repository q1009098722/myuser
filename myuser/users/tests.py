# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.urls import reverse

client = Client()

# Create your tests here.
class Test_Register(TestCase):
    def test_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "formc", status_code=200)
