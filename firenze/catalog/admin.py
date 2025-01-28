from django.contrib import admin
from django.utils.html import format_html
from catalog.models import (
    Product, 
    Color, 
    Material, 
    Size, 
    ProductType, 
    ProductTypePhotos, 
    Collections,
    ProductTypeShopLeft,
    Group,
)

class ProductTypeInline(admin.TabularInline):
    model = ProductType

    fields = ('name', 'size', 'color', 'material', 'price', 'list_image_tag', 'photo')
    readonly_fields = ('list_image_tag',)

    show_change_link = True
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        if (obj.photo):
            return format_html('<img style="max-width: 200px; " src="{}" />'.format(obj.photo.url))
        return ""
    def list_image_tag(self, obj):
        if (obj.photo):
            return format_html('<img style="max-width: 50px; " src="{}" />'.format(obj.photo.url))
        return ""
    image_tag.short_description = 'Фото'
    list_image_tag.short_description = 'Фото'

    readonly_fields = ('image_tag',)
    list_display = ['name', 'collection', 'list_image_tag', 'show_on_main_page', 'big_image']

    inlines = [ProductTypeInline]

admin.site.register(Product, ProductAdmin)

class ProductTypePhotosInline(admin.StackedInline):
    model = ProductTypePhotos
    extra = 0

class ProductTypeLeftInline(admin.StackedInline):
    model = ProductTypeShopLeft
    extra = 0

class ProuctTypeAdmin(admin.ModelAdmin):
    
    inlines = [ProductTypePhotosInline, ProductTypeLeftInline]

admin.site.register(ProductType, ProuctTypeAdmin)


admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Collections)
admin.site.register(Group)
admin.site.register(ProductTypeShopLeft)