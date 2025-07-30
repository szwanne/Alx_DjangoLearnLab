from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# /api/auth/token/ - POST endpoint for retrieving auth token
# Requires JSON body: {"username": "user", "password": "pass"}

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('auth/token/', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),  # Routes from the ViewSet (CRUD)
]
