from django.test import TestCase, Client
from django.urls import reverse


class TestShowsViewSet(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_last_shows_list(self):
        response = self.client.get(reverse('show-last'))
        self.assertLess(len(response.data), 10)
