from django.shortcuts import render
from django.core.signals import request_started
import requests
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Car
from django.http.response import JsonResponse
from .serializers import *
from django.core.mail import message


# Create your views here.
@api_view(['Get'])
def home(request):
    cars= Car.objects.all()
    print(cars)
    data={
        'cars':list(cars.values()),
    }
    return JsonResponse(data)


 
@api_view(['Get'])
def get_cars(request):
    cars= Car.objects.all()
    serializer= CarSer(cars,many=True)
    return Response(serializer.data)

 
    
@api_view(['Post'])    
def add_car(request):
    
    
    print(request.data)
    
    car = Car.objects.create(
        make=request.data.get('make'),
        model=request.data.get('model'),
        year=request.data.get('year'),
        color=request.data.get('color'),
        price=request.data.get('price'),
        is_available=request.data.get('is_available', True)
    )
    
    if car:
        return Response({"message": "Car added successfully", "car_id": car.id}, status=201)
    else:
        return Response({"message": "Failed to add car"}, status=400)
    
     
    
    
""" 
@api_view(['GET','PUT'])
def cars(request,pk):
    if(request.method == 'GET'):
        car=Car.objects.get(id=pk)
        ser=CarSer(car)
        Response(ser.data)
    if(request.method=='PUT'):
        car=Car.objects.get(id=pk) 
        ser=CarSer(car,data= request.data)
        if ser.is_valid():
            ser.save()
            Response(ser.data) 
        else:
            Response(ser.errors)     
  """
  
  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Car
from .serializers import CarSer
from django.http import Http404

@api_view(['GET', 'PUT', 'DELETE'])
def cars(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = CarSer(car)
        return Response(ser.data)

    elif request.method == 'PUT':
        ser = CarSer(car, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        carD=car.id
        car.delete()
        
        return Response({'message':f'car id {carD} deleted '}, status=status.HTTP_200_OK)
        
           


  
#_____________________class_based_view____________________________#


from rest_framework.views import APIView
class Car_view(APIView):
    def get(self,request):
        cars=Car.objects.all()
        ser=CarSer(cars,many=True)
        
        return Response({'Cars':ser.data},status=status.HTTP_200_OK)
        ser=CarSer(cars,many=True)
        
        return Response({'Cars':ser.data},status=status.HTTP_200_OK)
    def post(self,request):
        ser=CarSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'car':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors) 
        
        
        
class CarX(APIView):
    def found(self, pk):
        try:
            car = Car.objects.get(id=pk)
            return car
        except Car.DoesNotExist:
            return None

    def get(self, request, pk):
        car = self.found(pk)
        if car is None:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

        ser = CarSer(car)  # No need for many=True since it's a single object
        return Response({'Car': ser.data}, status=status.HTTP_200_OK)
    def put(self, request,pk):
        car = self.found(pk)
        if car is None:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
         
        ser = CarSer(car,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'Car update': ser.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Car update': ser.errors}, status=status.HTTP_204_NO_CONTENT)
    def delete(self, request,pk):
        car = self.found(pk)
        if car is None:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        carid=car.id 
        car.delete()
        return Response({'Car deleted':carid }, status=status.HTTP_200_OK)    
                             
                
        
          