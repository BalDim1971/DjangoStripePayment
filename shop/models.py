from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.template.defaultfilters import truncatewords
from pytils.translit import slugify

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    """
    Модель товара.
    Поля:
    name - название товара;
    description - описание товара;
    price - цена товара (пока руб.+коп.), изменить в зависимости от валюты.
    currency - валюта товара. Сделать список с выбором.
    Получать с сайта Stripe, если такая возможность есть.
    """
    
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Наименование')
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            validators=[
                                MinLengthValidator(5),
                                MaxLengthValidator(100),
                            ],
                            verbose_name='Slug')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='цена')
    currency = models.CharField(max_length=3, verbose_name='валюта')
    date_of_payment = models.DateField(verbose_name='дата оплаты')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name', 'date_of_payment')

    def __str__(self):
        return f'{self.name} - {truncatewords(self.description, 35)}'

    def get_display_price(self):
        return f'{self.price}'
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
