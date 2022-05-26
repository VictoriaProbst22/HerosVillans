from rest_framework import serializers
from .models import Super_types

class Super_TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_types
        fields =['type']
        