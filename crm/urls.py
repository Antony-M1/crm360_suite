from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include('crm.api.urls')),
    path('login',views.login)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)