from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        'title':'Home',
        'content': 'Welcome to the home page'
    }
    # add content only if user is logged in
    if request.user.is_authenticated():
        context['premium_content'] = 'YEAH'
    return render(request, 'home_page.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('error logging in')

    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        new_user = User.objects.create_user(username, email, password)
    return render(request, 'auth/register.html', context)

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
    return render(request, 'contact/view.html', context)