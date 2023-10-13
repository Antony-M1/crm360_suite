from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from crm.api.sidenav import SidebarView

urlpatterns = [
    path('', views.home),
    path('', include('crm.api.urls')),
    path('login',views.login),
    path('sign-up',views.signup),
    path('sidebar', SidebarView.as_view()),
    path('navbar',views.navbar)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)