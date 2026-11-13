from django.test import TestCase
from django.urls import reverse
from catalog.templatetags.catalog_filters import format_price


class CatalogViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Каталог библиотеки")

    def test_book_detail_view(self):
        response = self.client.get(reverse("catalog:book_detail"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "500 руб.")
        self.assertContains(response, "catalog/style.css")

    def test_book_list_view(self):
        response = self.client.get(reverse("catalog:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Список книг")
        self.assertContains(response, "Мастер и Маргарита")
        self.assertContains(response, "catalog/style.css")

    def test_format_price_filter(self):
        self.assertEqual(format_price(500), "500 руб.")
        self.assertEqual(format_price(1000, "₽"), "1000 ₽")
        self.assertEqual(format_price(None), "")
        self.assertEqual(format_price(""), "")

