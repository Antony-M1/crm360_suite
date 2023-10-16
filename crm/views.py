from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Masters
from crm.api.forms.auth import UserForm

# Create your views here.

def home(request):
    context = {}
    template_name = 'crm/index.html'
    # template_name = 'crm/navbar.html'
    context['side_nav_data']=sidebar({'type': 'M'})

    return render(request, template_name, context)


def login(request):
    return render(request, template_name='crm/login.html')


def signup(request):
    form = UserForm()
    return render(request, 'crm/signup.html', {'form': form})


def sidebar(req):
    side_nav = []

    if req.get('type'):
        data = Masters.objects.filter(type=req.get('type')).values()
        for i in data:
            d = {}
            d['name'] = i.get('name')
            d['path'] = i.get('path')
            side_nav.append(d)

    return side_nav
    
    
def navbar(request):
    return render(request, template_name='crm/navbar.html')
