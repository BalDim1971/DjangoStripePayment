from django.contrib import admin
from django.template.defaultfilters import truncatechars

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'description', 'currency',
                    'date_of_payment')
    list_filter = ('name',)
    list_display_links = ('pk', 'name')
    list_editable = ('price', 'description', 'currency')
    search_fields = ('name', 'description')
    list_per_page = 25
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    
    @admin.display(description='Краткое описание товара')
    def description_info(self, item: Item) -> str:
        return (f'Краткое описание товара: '
                f'{truncatechars(item.description, 35)}'
                )
