from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from autos.models import Auto
from autos.serializers import AutoSerializer

# Create your views here.

#Crear

class CrearAuto(APIView):
    permission_classes=(AllowAny,)

    def post(self, request):

        serializer=AutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'creado'})

#Listar

class ListaAuto(APIView):
    permission_classes=(AllowAny,)


    def get(self, request):
        atos_lista=Auto.objects.all()
        serializer=AutoSerializer(atos_lista, many=True)
        return Response(serializer.data)
    

#Actualizar 

class ActAutos(APIView):
    permission_classes=(AllowAny,)

    def get(self, request, auto_id):
        autos_lista = get_object_or_404(Auto, pk=auto_id)
        serializer = AutoSerializer(autos_lista)
        return Response(serializer.data)

    def put(self, request, auto_id):
        auto_obj=get_object_or_404(Auto, pk=auto_id)
        serializer= AutoSerializer(instance=auto_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
     
#Eliminar

class DelAutos(APIView):

    def get(self, request, auto_id):
        autos_lista = get_object_or_404(Auto, pk=auto_id)
        serializer = AutoSerializer(autos_lista)
        return Response(serializer.data)

    def delete(self, request, auto_id):
        auto_obj = get_object_or_404(Auto, pk=auto_id)
        auto_obj.status = False
        auto_obj.delete()
        return Response({'message':'Auto eliminado'}, status=status.HTTP_204_NO_CONTENT)
    

#Listar un solo auto.
    
class Lista1Auto(APIView):

    def get(self, request, auto_id):
        autos_lista = get_object_or_404(Auto, pk=auto_id)
        serializer = AutoSerializer(autos_lista)
        return Response(serializer.data)

         
         
             



