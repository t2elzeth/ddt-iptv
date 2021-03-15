from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .. import views


class TestUrls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url = reverse('show-last')
