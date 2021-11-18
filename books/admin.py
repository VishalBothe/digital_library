from django.contrib import admin
from .models import Book

# Register your models here.

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','tagline','author')
    list_display_links = ('title','tagline',)
    list_filter = ('category',)
    search_fields = ('title','category')