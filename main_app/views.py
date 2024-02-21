from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return render(request, "main/index.html")

def contact(request):
    return render(request, "main/contact.html")

def about(request):
    return render(request, "main/about.html")

def shop(request):
    return render(request, "main/shop.html")

def design(request):
    return render(request, "main/design.html")
