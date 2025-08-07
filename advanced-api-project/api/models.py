from django.db import models

# Author model with one-to-many relationship to Book


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model related to Author
# Book model represents a single book entity.
# Each book is linked to one Author via a ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
