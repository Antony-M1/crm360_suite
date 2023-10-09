from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, template_name='crm/index.html')


def login(request):
    return render(request, template_name='crm/login.html')