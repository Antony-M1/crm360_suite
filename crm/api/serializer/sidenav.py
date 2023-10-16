from rest_framework import serializers
from crm.models import Masters

class MastersSerializerType(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = ['name', 'path']