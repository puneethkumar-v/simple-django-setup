from django.shortcuts import render
# Create your views here.

def home_view(request):

        products = [
        {
            "id": 1,
            "name": "abc",
            "price": 100,
        },
        {
            "id": 2,
            "name": "abc",
            "price": 100,
        },
        {
            "id": 3,
            "name": "abc",
            "price": 100,
        },
    ]

    context = {
        "products": products,
    }
    return render(request, "base.html", context)