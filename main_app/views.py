from pipes import Template
from django.shortcuts import render, redirect
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response 
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # CUD
from django.contrib.auth import login # imported so that user is logged in immediately following sign up
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # protects view functions
from django.contrib.auth.mixins import LoginRequiredMixin # protects class-based views

# import model(s)
from .models import Application

# Create your views here.
# extending from View class
class Home(TemplateView):
    template_name = "home.html"

# Function view 
# GET all applications
@login_required
def applications_index(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'applications/index.html', { 'applications': applications})

# GET all incomplete applications
@login_required
def applications_ic(request):
    applications = Application.objects.filter(status='IC')
    applications = applications.filter(user=request.user)
    return render(request, 'applications/ic.html', { 'applications': applications})

# GET all applied applications
@login_required
def applications_a(request):
    applications = Application.objects.filter(status='A')
    applications = applications.filter(user=request.user)
    return render(request, 'applications/a.html', { 'applications': applications})

# GET all interviewed applications
@login_required
def applications_i(request):
    applications = Application.objects.filter(status='I')
    applications = applications.filter(user=request.user)
    return render(request, 'applications/i.html', { 'applications': applications})

# GET all offered applications
@login_required
def applications_o(request):
    applications = Application.objects.filter(status='O')
    applications = applications.filter(user=request.user)
    return render(request, 'applications/o.html', { 'applications': applications})

# GET all rejected applications
@login_required
def applications_r(request):
    applications = Application.objects.filter(status='R')
    applications = applications.filter(user=request.user)
    return render(request, 'applications/r.html', { 'applications': applications})

# Class-based views (CBVs) 

# CREATE one application
class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['company', 'position', 'application_link', 'location', 'status', 'date_applied', 'notes']

    # override CreateView's form_valid method to assign the logged in user (self.request.user)
    def form_valid(self, form):
        # assign the logged in user (where the form.instance is the application)
        form.instance.user = self.request.user
        # super() to invoke methods inherited by the superclass
        return super().form_valid(form)

# UPDATE one application
class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ['company', 'position', 'application_link', 'location', 'status', 'date_applied', 'notes']

# DELETE one application
class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    fields = '__all__'
    success_url = '/applications/' # reference path with success url

# SIGN UP (Note: Log in is predefined by Django auth)
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # this is how to create a 'user' form object
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # add user to the database
            user = form.save()
            #log a user in 
            login(request, user)
            return redirect('applications_index') # reference name of url path with redirect
        else:
            error_message = 'Invalid sign up. Please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)