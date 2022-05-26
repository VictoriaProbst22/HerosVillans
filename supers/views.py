from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.serializers import Super_TypesSerializer
from .serializers import SuperSerializer
from .models import Super
from supers import serializers



@api_view(['GET', 'POST'])
def Supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers);
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)