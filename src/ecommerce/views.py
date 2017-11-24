from django.http import HttpResponse
from django.shortcuts import render


from .forms import ContactForm

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
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':'Contact',
        'contact_form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)        
    # if request.method == 'POST':
    #     for key in ['fullname', 'email', 'content']:
    #         print(request.POST.get(key))
    return render(request, "contact/view.html", context)