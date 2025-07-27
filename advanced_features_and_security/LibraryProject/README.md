Introduction to Django Development Environment Setup

Objective: To gain familiarity with Django by setting up a Django development environment and creating a basic Django project. This task aims to introduce you to the workflow of Django projects, including project creation and running the development server.

Task Description: Install Django and create a new Django project named LibraryProject. This initial setup will serve as the foundation for developing Django applications. You’ll also explore the project’s default structure to understand the roles of various components.

# Permissions and Groups Setup

## Groups

- **Viewers**: Can only view books (`can_view`)
- **Editors**: Can view, create, and edit books (`can_view`, `can_create`, `can_edit`)
- **Admins**: Full control (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Usage

- Assign users to groups via Django Admin → Users → Groups.
- Views are protected with the `@permission_required` decorator checking appropriate permissions.
- Unauthorized users receive an error (HTTP 403) when trying to access restricted views.

## Adding Permissions

- Permissions are defined in the `Book` model's `Meta` class.
- New permissions require running migrations and updating group assignments.

# ✅ DEBUG should be False in production to avoid exposing sensitive error info

DEBUG = False

# ✅ Enforce secure cookies over HTTPS

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
