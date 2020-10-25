from django.contrib import admin
from .models import  Banner, Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name', 'is_publish', 'description', 'price',  'date')
    list_display_links=('id','name')
    list_editable=('is_publish',)
    search_fields=('name', 'description', 'price')
    list_per_page=25

admin.site.register(Banner)
admin.site.register(Product, ProductAdmin)
