from django.test import TestCase
from django.urls import reverse
from django.conf import settings
import json
from copy import copy


VALID_USER = {'email': 'yaroslav@kkk.com',
              'password': 'A12345678',
              'first_name': 'yaroslav',
              'last_name': 'chyhryn'}


class AccountsViewTest(TestCase):

    def test_valid_user(self):
        resp = self.client.post(reverse('accounts:register'),
                                json.dumps(VALID_USER),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_email_validation(self):
        invalid_emails = ['', '34234dd', 'blahblah@gmail.com', 'blahblah@icloud.com']

        for email in invalid_emails:
            test_user = copy(VALID_USER)
            test_user['email'] = email

            resp = self.client.post(reverse('accounts:register'),
                                    json.dumps(test_user),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)

    def test_password_validation(self):
        invalid_passwords = ['', 'aaaaaaaaaaa', 'fre4___u+']

        for password in invalid_passwords:
            test_user = copy(VALID_USER)
            test_user['password'] = password

            resp = self.client.post(reverse('accounts:register'),
                                    json.dumps(test_user),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)

    def test_first_name_validation(self):
        invalid_first_names = ['121321321', 'asdf3234+++']

        for first_name in invalid_first_names:
            test_user = copy(VALID_USER)
            test_user['first_name'] = first_name

            resp = self.client.post(reverse('accounts:register'),
                                    json.dumps(test_user),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)

    def test_last_name_validation(self):
        invalid_last_names = ['123', 'ssss555']

        for last_name in invalid_last_names:
            test_user = copy(VALID_USER)
            test_user['last_name'] = last_name

            resp = self.client.post(reverse('accounts:register'),
                                    json.dumps(test_user),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)
