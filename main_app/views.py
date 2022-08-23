from pipes import Template
from django.shortcuts import render
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response 
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import model(s)
from .models import Application

# Create your views here.
# extending from View class
class Home(TemplateView):
    template_name = "home.html"

class GetStarted(TemplateView):
    template_name = "get-started.html"

# Class-based views (CBVs) 
# GET all applications
class ApplicationList(ListView):
    model = Application
    fields = '__all__'

# GET one application
class ApplicationDetail(DetailView):
    model = Application
    fields = '__all__'

# CREATE one application
class ApplicationCreate(CreateView):
    model = Application
    fields = ['company', 'position', 'application_link', 'location', 'status', 'date_applied', 'notes']

    # override CreateView's form_valid method to assign the logged in user (self.request.user)
    def form_valid(self, form):
        # assign the logged in user (where the form.instance is the application)
        form.instance.user = self.request.user
        # super() to invoke methods inherited by the superclass
        return super().form_valid(form)

# UPDATE one application
class ApplicationUpdate(UpdateView):
    model = Application
    fields = '__all__'

# DELETE one application
class ApplicationDelete(DeleteView):
    model = Application
    fields = '__all__'
