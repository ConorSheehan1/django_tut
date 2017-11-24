from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        'title':'Home',
        'content': 'Welcome to the home page'
    }
    return render(request, 'home_page.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    # print(request.user.is_authenticated())
    if form.is_valid():
        # print(request.user.is_authenticated())
        # print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login')
        else:
            print('error logging in')

    return render(request, 'auth/login.html', context)

def regester_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'auth/register.html', {})

def about_page(request):
    context = {
        'title':'About'
    }
    return render(request, 'home_page.html', context)

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
    return render(request, 'contact/view.html', context)