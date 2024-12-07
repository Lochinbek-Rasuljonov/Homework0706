from django.contrib import admin
from django.utils.html import mark_safe
from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'year', 'color', 'engine_type', 'mileage', 'transmission', 'image_preview')

    def engine_type_display(self, obj):
        return obj.get_engine_type_display()

    def transmission_display(self, obj):
        return obj.get_transmission_display()

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px" height="100px" />')
        return "No image"
    image_preview.short_description = 'Image Preview'

    list_display += ('engine_type_display', 'transmission_display')

    search_fields = ['name', 'brand__name', 'description']
    list_filter = ('brand', 'engine_type', 'transmission', 'year')


    list_per_page = 7