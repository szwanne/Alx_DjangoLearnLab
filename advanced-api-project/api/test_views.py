from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name='J.K. Rowling')

        # Create books
        self.book1 = Book.objects.create(
            title='Harry Potter 1', publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(
            title='Harry Potter 2', publication_year=1998, author=self.author)

        self.book_create_url = reverse('book-create')
        self.book_list_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse(
            'book-detail', kwargs={'pk': pk})
        self.book_update_url = lambda pk: reverse(
            'book-update', kwargs={'pk': pk})
        self.book_delete_url = lambda pk: reverse(
            'book-delete', kwargs={'pk': pk})

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter 1')

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'Updated Title',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.put(self.book_update_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.book_delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(
            f'{self.book_list_url}?publication_year=1998')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 2')

    def test_search_books_by_title(self):
        response = self.client.get(f'{self.book_list_url}?search=Harry')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_title_desc(self):
        response = self.client.get(f'{self.book_list_url}?ordering=-title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 2')
