from rest_framework.decorators import api_view
from rest_framework.response import Response

from supers import serializers
from .serializers import Super_TypesSerializer
from .models import Super_types

@api_view(['GET'])
def super_type_list(request):
    super_type = Super_types.objects.all()

    serializer = Super_TypesSerializer(super_type, many=True)

    return Response(serializer.data)
