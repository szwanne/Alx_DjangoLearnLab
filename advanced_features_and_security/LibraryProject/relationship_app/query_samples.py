from relationship_app.models import Author, Book, Library, Librarian
import os
import django

# replace with your actual project name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()


# Setup sample data

def setup_sample_data():
    author1 = Author.objects.create(name="Chinua Achebe")
    author2 = Author.objects.create(name="J.K. Rowling")

    book1 = Book.objects.create(title="Things Fall Apart", author=author1)
    book2 = Book.objects.create(title="No Longer at Ease", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)

    library = Library.objects.create(name="Central Library")
    library.books.set([book1, book2, book3])

    librarian = Librarian.objects.create(name="Sipho Zwane", library=library)

# Query 1: All books by a specific author


# def get_books_by_author(author_name):
#     books = Book.objects.filter(author__name=author_name)
#     print(f"\nBooks by {author_name}:")
#     for book in books:
#         print(f"- {book.title}")

# Query 2: All books in a library


def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")

# Query 3: Get the librarian for a library


def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or librarian not found.")


def find_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(f"Book: {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")


# Run all
if __name__ == "__main__":
    setup_sample_data()
    # get_books_by_author("Chinua Achebe")
    find_books_by_author("Chinua Achebe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
