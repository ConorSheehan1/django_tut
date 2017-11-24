from django.http import HttpResponse
from django.shortcuts import render

def home_page(reguest):
    return render(reguest, "home_page.html", {})