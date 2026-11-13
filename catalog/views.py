from django.shortcuts import render


def book_list(request):
    books = [
        {
            "title": "Мастер и Маргарита",
            "author": "Михаил Булгаков",
            "year": 1967,
            "description": "Роман Михаила Афанасьевича Булгакова.",
            "price": 500,
        },
        {
            "title": "Преступление и наказание",
            "author": "Федор Достоевский",
            "year": 1866,
            "description": "Социально-психологический роман.",
            "price": 450,
        },
    ]
    return render(request, "catalog/book_list.html", {"books": books})


def index(request):
    return book_list(request)


def book_detail(request, book_id=1):
    book = {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967,
        "description": "Роман Михаила Афанасьевича Булгакова.",
        "price": 500,
    }
    return render(request, "catalog/book_detail.html", {"book": book})
