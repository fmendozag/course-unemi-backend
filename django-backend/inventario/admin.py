from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProductoCategoria)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'categoria',
        'stock_disponible',
        'precio'
    )
    list_per_page = 20
    search_fields = ('codigo','nombre')
    list_filter = (
        'categoria',
        'estado'
    )

admin.site.register(Producto,ProductoAdmin)
