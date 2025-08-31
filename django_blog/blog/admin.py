from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('short', 'post', 'author', 'created_at')
    search_fields = ('content', 'author__username', 'post__title')

    def short(self, obj):
        return (obj.content[:50] + '...') if len(obj.content) > 50 else obj.content
    short.short_description = 'Comment'
