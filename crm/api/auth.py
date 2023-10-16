from rest_framework import routers, serializers, viewsets
from crm.models import UserAU
from crm.api.forms.auth import UserForm
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
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  
            user.save()  
            return redirect("/login")
        else:
            return render(request, 'crm/signup.html', {'form': form})
    else:
        
        form = UserForm()
    return render(request, 'signup.html', {'form': form})