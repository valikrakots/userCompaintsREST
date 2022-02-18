import json

from django.test.testcases import TestCase

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestTicketApi(TestCase):                            #testing if unauthenticated user can get or post tickets

    def setUp(self):
        self.client = APIClient()

    def testUnregistered(self):
        response1 = self.client.get(reverse('ticketslist'))

        data_json = {
            'title': 'Problem',
            'content': 'Problem',
        }
        response2 = self.client.post(reverse('ticketslist'), data=data_json, format='json')
        assert response1.status_code == 401
        assert response2.status_code == 401

