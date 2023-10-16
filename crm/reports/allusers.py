from django.shortcuts import render
from crm.models import UserAU
from django.db import connection

def allusers(request):
    columns = ['name','email','joining_date']
    # raw_query = "SELECT username, email, DATE(date_joined) FROM \"tabUser\""
    # with connection.cursor() as cursor:
    #     cursor.execute(raw_query)
    #     data = cursor.fetchall()
    # kk = data
    data = UserAU.objects.values_list('username','email','date_joined')
    

    context = {
        'columns': columns,
        'data': data
    }
    return context