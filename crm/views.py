from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Masters

# Create your views here.

def home(request):
    context = {}
    # template_name = 'crm/index.html'
    template_name = 'crm/navbar.html'
    context['side_nav_data']=sidebar({'type': 'M'})

    return render(request, template_name, context)


def login(request):
    return render(request, template_name='crm/login.html')


def signup(request):
    return render(request, template_name='crm/signup.html')

def sidebar(req):
    side_nav = []

    if req.get('type'):
        data = Masters.objects.filter(type=req.get('type')).values()
        for i in data:
            side_nav.append(i.get('name'))

    return side_nav
    
    
def navbar(request):
    return render(request, template_name='crm/navbar.html')
