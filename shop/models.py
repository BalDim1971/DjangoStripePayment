from django.db import models


class Item(models.Model):
    """
    Модель товара.
    Поля:
    name - название товара;
    description - описание товара;
    price - цена товара (пока руб.коп., развернуть в зависимости от валюты).
    """
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f'{self.price} '
