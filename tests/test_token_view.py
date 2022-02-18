import json

from django.test.testcases import TestCase

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestTokenApi(TestCase):                                                        #testing if user can register and get his own token
    def setUp(self):
        self.client = APIClient()

    def testRegistration(self):
        data_json = {
            'email': '1234@dd.com',
            'password': '12345678',
        }
        expected_json = {
            'email': '1234@dd.com',
        }
        response = self.client.post(reverse('create_user'), data=data_json, format='json')
        assert response.status_code == 201
        assert json.loads(response.content) == expected_json
        response = self.client.post(reverse('token_create'), data=data_json, format='json')
        assert response.status_code == 200










