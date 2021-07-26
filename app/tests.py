from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class TestStatusView(TestCase):

    def test_status_view(self):
        response = self.client.get(
            path=reverse("status")
        )

        # assert request.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'All is OK!')
