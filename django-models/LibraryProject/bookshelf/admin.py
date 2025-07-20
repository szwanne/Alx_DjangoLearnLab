from django.contrib import admin

# Register your models here.
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show columns
    list_filter = ('publication_year', 'author')            # filter sidebar
    search_fields = ('title', 'author')                     # search bar
