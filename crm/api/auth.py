from rest_framework import routers, serializers, viewsets
from crm.models import UserAU


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