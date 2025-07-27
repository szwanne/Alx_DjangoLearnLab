from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# -------------------------------
# Custom User Manager
# -------------------------------


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(username, email, password, **extra_fields)

# -------------------------------
# Custom User Model
# -------------------------------


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='Member')

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email', 'date_of_birth']
    USERNAME_FIELD = 'username'  # You can switch to 'email' if preferred

    def __str__(self):
        return f"{self.username} ({self.role})"

# -------------------------------
# Author, Book, Library, Librarian Models
# -------------------------------


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name='librarian'
    )

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomUserManager()


# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.db import models
# from django.contrib.auth.models import User

# # Authors Model.


# class Author(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# # Books Model


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(
#         Author, on_delete=models.CASCADE, related_name='books'
#     )

#     def __str__(self):
#         return self.title

#     class Meta:
#         permissions = [
#             ("can_add_book", "Can add book"),
#             ("can_change_book", "Can change book"),
#             ("can_delete_book", "Can delete book"),
#         ]

# # Library Model


# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     books = models.ManyToManyField(Book, related_name='libraries')

#     def __str__(self):
#         return self.name

# # Librarian Model


# class Librarian(models.Model):
#     name = models.CharField(max_length=100)
#     library = models.OneToOneField(
#         Library, on_delete=models.CASCADE, related_name='librarian'
#     )

#     def __str__(self):
#         return self.name


# class UserProfile(models.Model):
#     ROLE_CHOICES = (
#         ('Admin', 'Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
#     )

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"

# # Django signal to automatically create a UserProfile when a new user is created


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()
