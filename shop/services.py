"""
Сервисные функции проведения оплаты товара.
"""

import stripe
import logging
from config.settings import STRIPE_SECRET
from .models import Item


stripe.api_key = STRIPE_SECRET
logger = logging.getLogger('Запуск сессии для оплаты товара')


def create_stripe_price(item: Item) -> str:
    """
    Создаем запрос для товара.
    :param item: Item: описание товара.
    :return:
    """
    logger.info(f'Создаем запрос для оплаты товара: {item.name}')
    stripe_product: stripe.Product = stripe.Product.create(name=item.name)
    stripe_price: stripe.Price = stripe.Price.create(
        currency='rub',
        unit_amount=int(item.price) * 100,
        product_data={'name': stripe_product['name']},
    )
    return stripe_price['id']


def create_stripe_session(stripe_price_id: stripe.Price) -> tuple[str, str]:
    """
    Создаем сессию для проверки.
    """
    logger.info(f'Создаем сессию для оплаты товара: {stripe_price_id}')
    try:
        stripe_session: stripe.Session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': stripe_price_id.name,
                        'description': stripe_price_id.description,
                    },
                    'unit_amount': stripe_price_id.unit_amount,
                },
                'quantity': 1
            }],
            mode='payment',
            success_url='https://example.com/success',
        )
    except Exception as exc:
        logger.error(f'Исключение {exc} сгенерировано')
        return "Не смогли найти сессию.", ""
    logger.info(f'Сессия успешно создано для товара: {stripe_price_id.name}')
    
    return stripe_session['url'], stripe_session['id']
