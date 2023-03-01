from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Product
from src.user.models import User


class ProductTest(APITestCase):
    def setUp(self):
        self.profile1 = User.objects.create(
            username='username1',
            first_name='test',
            last_name='test',
            middle_name='test',
            email='test1@mail.ru',
            phone='+798199944009',
            password='test1'
        )
        self.profile1.save()
        self.profile1_token = Token.objects.create(user=self.profile1)

        self.profile2 = User.objects.create(
            username='username2',
            first_name='test2',
            last_name='test2',
            middle_name='test2',
            email='test2@mail.ru',
            phone='+79819993333',
            password='test1'
        )
        self.profile4.save()

        self.product = Product.objects.create(
            name='test',
            price=1,
        )

    def test_product_list(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.profile1_token.key)
        response = self.client.get(reverse('product_list'))
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.status_code, 200)

    def test_my_team_no_authorization(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 401)