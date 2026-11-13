from django.contrib import admin
from django.urls import include, path
from catalog import views as catalog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
    path("", catalog_views.book_list, name="book_list"),
    path("book/", catalog_views.book_detail, name="book_detail"),
]
