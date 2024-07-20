from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.

class SignupView(CreateView):

    form_class= UserCreationForm
    template_name= "registration/signup.html"
    success_url=reverse_lazy("login")

class FirstPage(TemplateView):

    template_name= "registration/first_page.html"

class LogoutPageView(TemplateView):
    
    template_name= "registration/logout.html"


