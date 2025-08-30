from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add the extra fields to the admin form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
         'fields': ('bio', 'profile_picture', 'followers')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
         'fields': ('bio', 'profile_picture', 'followers')}),
    )
    list_display = ['username', 'email',
                    'is_staff', 'bio']  # Customize list view


admin.site.register(CustomUser, CustomUserAdmin)
