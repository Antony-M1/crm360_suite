from crm.api.serializer.sidenav import MastersSerializerType
from crm.models import Masters


from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions

class SidebarView(APIView):

    def post(self, req):
        data = req.data

        if data.get('type'):
            data = Masters.objects.filter(type=data.get('type')).values()
        serializer = MastersSerializerType(data, many = True)
        return Response(serializer.data)