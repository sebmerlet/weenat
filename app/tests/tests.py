import json
from rest_framework.test import RequestsClient
from django.test import TestCase

from app.models import Users
from app.serializers import UsersDetailSerializer


class UsersTestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()

        # data for list test
        with open("app/tests/users_test.json", 'r') as txt:
            users = json.loads(txt.read())
        for user in users:
            Users.objects.create(**user)

        # Add serializer for detail view
        self.serializer = UsersDetailSerializer(instance=Users.objects.first())

    def tearDown(self):
        del self.serializer

    def test_list(self):
        resp = self.client.get('http://testserver/users/')
        self.assertEqual(resp.status_code, 200, 'Get request ok')

    def test_detail(self):
        resp = self.client.get('http://testserver/users/1/')
        keys_view = list(resp.json().keys())
        keys_fields = [key for key in self.serializer.fields.keys()]
        self.assertEqual(resp.status_code, 200, 'Detail request ok')
        self.assertListEqual(keys_view, keys_fields, 'Check fields keys in detail view')

    def test_filter(self):
        resp = self.client.get('http://testserver/users/?year=1976')
        self.assertEquals(len(resp.json()), 2, "Number of users born in 1976: 2")

    def test_users_model(self):
        user = Users()
        self.assertTrue(hasattr(user, 'birthday'), "Birthday field exists")
