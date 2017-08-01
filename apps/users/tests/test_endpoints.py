# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from apps.users.models import User
from apps.core.tests import base


class AuthUsersTestCase(base.BaseTestCase):
    model = User
    inactive_user = {
        'email': 'inactive@devslaw.com',
        'password': 'pass1234',
        'is_active': False
    }

    active_user = {
        'email': 'active@devslaw.com',
        'password': 'pass1234',
        'is_active': True
    }

    signup_user = {
        'email': 'signup@devslaw.com',
        'password': 'pass1234',
        'phone': '12345',
    }

    def setUp(self):
        super().setUp()

        self.__add_data_to_db()

    def test_get_auth_token_200(self):

        data = {
            'username': self.admin_user['email'],
            'password': self.admin_user['password'],
        }
        response = self.client.post(reverse('users:login'), data)
        self.assertEqual(response.status_code, 200)

    def test_get_auth_token_400(self):

        invalid_data = [
            {
                'main_data': {
                    'username': 'invalid_email',
                    'password': 'invalid_password'
                },
                'message': '{"non_field_errors":["Unable to log in with provided credentials."]}'
            },
            {
                'main_data': {
                    'username': 'test_email',
                },
                'message': '{"password":["This field is required."]}',
            },
            {
                'main_data': {
                    'password': 'test_password',
                },
                'message': '{"username":["This field is required."]}',
            },
            {
                'main_data': {
                    'username': self.inactive_user['email'],
                    'password': self.inactive_user['password'],
                },
                'message': '{"non_field_errors":["User account is disabled."]}'
            },
        ]

        for data in invalid_data:
            response = self.client.post(reverse('users:login'), data['main_data'])
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.content.decode('utf-8'), data['message'])

    def test_forgot_password_200(self):

        data = {
            'main_data': {
                'email': self.active_user['email']
            },
            'result': '{"result": "success"}'
        }

        response = self.client.post(reverse('users:forgot_password'), data['main_data'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), data['result'])

    def test_forgot_password_400(self):

        invalid_data = [
            {
                'main_data': {
                    'email': 'invalid_email'
                },
                'message': '{"email":["Enter a valid email address."]}'
            },
            {
                'main_data': {
                    'email': self.inactive_user['email']
                },
                'message': '{"non_field_errors":["Your account is inactive."]}'
            },
            {
                'main_data': {
                    'email': 'email_does_not_exist@devslaw.com'
                },
                'message': '{"non_field_errors":["This email address does not exist."]}'
            }
        ]

        for data in invalid_data:
            response = self.client.post(reverse('users:forgot_password'), data['main_data'])
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.content.decode('utf-8'), data['message'])

    def test_sign_up_200(self):

        data = {
            'main_data': {
                'email': self.signup_user['email'],
                'password': self.signup_user['password'],
                'repeat_password': self.signup_user['password'],
            },
            'result': '{"result": "success"}'
        }

        response = self.client.post(reverse('users:signup'), data['main_data'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), data['result'])

    def test_sign_up_400(self):

        invalid_data = [
            {
                'main_data': {
                    'email': self.signup_user['email'],
                    'password': self.signup_user['password'],
                },
                'message': '{"repeat_password":["This field is required."]}'
            },
            {
                'main_data': {
                    'email': self.signup_user['email'],
                    'password': self.signup_user['password'],
                    'repeat_password': 'invalid_password',
                },
                'message': '{"non_field_errors":["Password and Repeat Password fields must match."]}'
            },
            {
                'main_data': {
                    'email': self.inactive_user['email'],
                    'password': self.signup_user['password'],
                    'repeat_password': self.signup_user['password'],
                },
                'message': '{"non_field_errors":["This email address has already exist."]}'
            },
        ]

        for data in invalid_data:
            response = self.client.post(reverse('users:signup'), data['main_data'])
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.content.decode('utf-8'), data['message'])

    def __add_data_to_db(self):

        self.model.objects.create_user(**self.inactive_user)
        self.model.objects.create_user(**self.active_user)
