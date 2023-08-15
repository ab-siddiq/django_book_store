from django.urls import path
from book.views import home,store_book
urlpatterns = [
    path('',home,name='home'),
    path('store_new_book/',store_book,name="store_new_book"),
    path('view_book/',store_book,name="view_book"),
    path('show_books/',store_book,name="show_books"),
]
