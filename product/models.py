from django.db import models


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    create_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата редактирования", auto_now_add=True)
    is_active = models.BooleanField('Активность', default=True)

    def __str__(self):
        return self.name
