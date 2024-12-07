from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageVierw(TemplateView):
    template_name = "home.html"

class AboutPageVierw(TemplateView):
    template_name = "about.html"