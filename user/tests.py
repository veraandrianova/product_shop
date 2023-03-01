from rest_framework.test import APITestCase

from .models import User


user_create_data = {
    'username': 'username1',
    'first_name': 'test',
    'last_name': 'test',
    'middle_name': 'test',
    'email': 'test1@mail.ru',
    'phone':'+798199944009',
    'password':'test1'
}


class ProfileAuthTests(APITestCase):
    def setUp(self):
        self.client.post('/api/v1/auth/users/', user_create_data, format='json')
        url = "/api/v1/auth/token/login/"
        user = {
            'username': user_create_data['email'],
            'password': user_create_data['password']
        }
        response = self.client.post(url, user, format='json')
        self.assertEqual(response.status_code, 200)


class ProfileRegTests(APITestCase):
    def test_create_user(self):
        self.client.post('/api/v1/auth/users/', user_create_data, format='json')
        user = User.objects.get(email='test1@mail.ru')
        self.assertEqual(user.username, 'username1')
        self.assertEqual(user.email, 'test1@mail.ru')

    def test_create_user_error_pass(self):
        data = user_create_data.copy()
        data['re_password'] = 'V97tn7M4ru'
        request = self.client.post('/api/v1/auth/users/', data, format='json')
        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.data['non_field_errors'][0].title(), 'Два Пароля Не Совпадают.')
