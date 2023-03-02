from typing import overload
from django.conf import settings

from src.product.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.total_prise = 0

    def getter(self):
        for key, value in self.cart:
            self.total_prise += int(value['price'])
        return self.total_prise

    @overload
    def add(self, product: Product, quantity: int = 1, update_quantity=False) -> None:

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):

        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):

        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

@overload
def some_function(value: int) -> int: ...
@overload
def some_function(value: float) -> float: ...
@overload
def some_function(value: str) -> str: ...


def some_function(value):
    if isinstance(value, int):
        return value + 1
    elif isinstance(value, float):
        return value * 2.0
    elif isinstance(value, str):
        return "Hello, " + value
    else:
        raise TypeError