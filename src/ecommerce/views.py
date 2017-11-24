from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'title':'Home',
        'content': 'Welcome to the home page'
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        'title':'About'
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    context = {
        'title':'Contact'
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, "contact/view.html", context)