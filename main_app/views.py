from django.shortcuts import render
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response 
from django.views.generic.base import TemplateView

# Create your views here.
# extending from View class
class Home(TemplateView):
    template_name = "home.html"