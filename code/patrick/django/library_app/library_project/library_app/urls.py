from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, profile, CheckoutListView, HomePageView
from django.urls import path

urlpatterns = [
    path('', HomePageView, name='home'),
    path('author_list/', AuthorListView.as_view(), name='author_list'),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    # path('books/<author>/', AuthorBookListView.as_view(), name='author_book'),
    path('profile/', profile, name='profile'),
    path('checkout_list/', CheckoutListView.as_view(), name='checkout')
    
    
]