from django.contrib import admin

from catalog import models


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pizza_type', 'dough_type', 'size')
    list_filter = ('pizza_type', 'dough_type', 'size')
    search_fields = ('name', )
    ordering = ('id', )
    list_editable = ('pizza_type', 'dough_type', 'size')


admin.site.register(models.Pizza, PizzaAdmin)
