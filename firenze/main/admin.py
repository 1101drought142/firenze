from django.contrib import admin
from django.utils.html import format_html
from main.models import (
    News, 
    NewsPhotos,
    Shops
)
class NewsPhotosInline(admin.StackedInline):
    model = NewsPhotos
    extra = 0
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsPhotosInline]

admin.site.register(News, NewsAdmin)
admin.site.register(Shops)