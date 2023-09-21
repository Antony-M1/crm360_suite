from django.contrib import admin
from .models import (
    UserAU,
    Salutation,
    Gender,
    LeadSource,
    Customer,
    Territory
)

# Register your models here.
admin.AdminSite.site_header = 'CRM360 Admin Pannel'


class AdminUserAU(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    prepopulated_fields = {'email': ('email',)}
    
admin.site.register(UserAU, AdminUserAU)


class AdminSalutation(admin.ModelAdmin):
    list_display = ('salutation',)
    list_filter = ('salutation',)
    search_fields = ('salutation',)
    prepopulated_fields = {'salutation': ('salutation',)}
    
admin.site.register(Salutation, AdminSalutation)


class AdminGender(admin.ModelAdmin):
    list_display = ('gender',)
    list_filter = ('gender',)
    search_fields = ('gender',)
    prepopulated_fields = {'gender': ('gender',)}

admin.site.register(Gender, AdminGender)


class AdminLeadSource(admin.ModelAdmin):
    list_display = ('source_name','details')
    list_filter = ('source_name','details')
    search_fields = ('source_name',)
    prepopulated_fields = {'source_name': ('source_name',)}
    
admin.site.register(LeadSource, AdminLeadSource)


class AdminCustomer(admin.ModelAdmin):
    list_display = ('customer_name','customer_type')
    list_filters = ('customer_name','customer_type')
    search_fields = ('customer_name','customer_type')
    
admin.site.register(Customer, AdminCustomer)


class AdminTerritory(admin.ModelAdmin):
    
    list_display = ('name',)
    list_filters = ('name',)
    search_fields = ('name',)
    
admin.site.register(Territory, AdminTerritory)