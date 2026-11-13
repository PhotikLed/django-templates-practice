from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("", views.index, name="index"),
    path("books/", views.book_list, name="books"),
    path("book/", views.book_detail, name="book_detail"),
    path("book/<int:book_id>/", views.book_detail, name="book_detail_by_id"),
]
