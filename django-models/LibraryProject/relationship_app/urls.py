from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library_detail'),
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]
