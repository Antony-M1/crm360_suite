from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from crm.api.sidenav import SidebarView
from crm.reports import report_views


urlpatterns = [
    path('', views.home),
    path('', include('crm.api.urls')),
    path('2',report_views.allusers),
    path('python',report_views.allusers),
    path('login',views.login),
    path('sign-up',views.signup),
    path('sidebar', SidebarView.as_view()),
    path('navbar',views.navbar)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)