from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'


class YourAppConfig(AppConfig):
    name = 'yourapp'

    def ready(self):
        # Create groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        book_ct = ContentType.objects.get(app_label='yourapp', model='book')

        # Get permissions
        can_view = Permission.objects.get(
            codename='can_view', content_type=book_ct)
        can_create = Permission.objects.get(
            codename='can_create', content_type=book_ct)
        can_edit = Permission.objects.get(
            codename='can_edit', content_type=book_ct)
        can_delete = Permission.objects.get(
            codename='can_delete', content_type=book_ct)

        # Assign permissions to groups
        editors.permissions.set([can_edit, can_create])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])
