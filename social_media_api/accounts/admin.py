# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import Follow  # optional: register the Follow model in admin

User = get_user_model()


class FollowInline(admin.TabularInline):
    model = Follow
    fk_name = "follower"   # show who the user is following (adjust if needed)
    extra = 0
    verbose_name = "Following"
    verbose_name_plural = "Following"


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)
    inlines = (FollowInline,)  # optional — remove if you don't want inline


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "followed", "created_at")
    search_fields = ("follower__username", "followed__username")
    readonly_fields = ("created_at",)
