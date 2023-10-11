from rest_framework import routers, serializers, viewsets
from crm.models import UserAU
from crm.api.forms.auth import SineUpForm
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from crm.models import UserAU
from django.shortcuts import render,redirect
from django.contrib import messages
import json



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAU
        fields = ['username', 'email', 'is_staff']
        
        
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAU.objects.all()
    serializer_class = UserSerializer
    

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)




def signup(request):
    if request.method == "POST":
        form = SineUpForm(request.POST)
        if form.is_valid():
            user = UserAU(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/login")  
        else:
            query_params = {
                'first_name': request.POST.get('first_name', ''),
                'last_name': request.POST.get('last_name', ''),
                'email': request.POST.get('email', ''),
                'errors': form.errors.as_json(),
            }
            redirect_url = f"/sign-up?{'&'.join([f'{key}={value}' for key, value in query_params.items()])}"
            return HttpResponseRedirect(redirect_url)
    else:
        
        form = SineUpForm()
    return render(request, 'signup.html', {'form': form})