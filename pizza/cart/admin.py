from django.contrib import admin

from cart import models


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pizza', 'count')
    list_display_links = ('user', 'pizza')
    search_fields = ('user', 'pizza')
    ordering = ('user',)


admin.site.register(models.Cart, CartAdmin)
