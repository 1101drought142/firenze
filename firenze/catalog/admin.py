from django.contrib import admin
from catalog.models import Product, Color, Material, Size, ProductType, ProductTypePhotos

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(ProductType)
admin.site.register(ProductTypePhotos)
