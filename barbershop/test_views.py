import unittest
from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse


class PagesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_error_404(self):
        response = self.client.get('/wierdstuff/')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(response, '404.html')


if __name__ == '__main__':
    unittest.main()
