import logging

from django.shortcuts import get_object_or_404, render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from config.settings import STRIPE_PUBLIC
from .models import Item
from .services import create_stripe_session

logger = logging.getLogger('item')


class ItemDetailView(GenericAPIView):
    """
    Детальный просмотр данных о товаре.
    """
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'items/item_detail.html', {'item': item, 'stripe_key': STRIPE_PUBLIC})


class ItemBuyView(GenericAPIView):
    """
    Возвращает идентификатор сессии покупки товара.
    """
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        session = create_stripe_session(item)
        logger.info(f'checkout session for {item} is {session.id}')
        return Response({"session_id": session.id})