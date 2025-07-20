# Admin Customization for Book Model

## Admin Configuration (bookshelf/admin.py)

```python
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
```
