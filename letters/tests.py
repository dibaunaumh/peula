"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_org_page(self):
        """
        Tests the model of the organization page.
        """
        url = "/organization/Sony"
        c = Client()
        response = c.get(url)
        org = response.context["organization"]
        self.assertEquals("Sony", org.name)
        self.assertEquals("info@sony.com", org.email)


