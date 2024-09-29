from django.shortcuts import render

# Create your views here.
from .models import Manager, Employee
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import uuid

@api_view(['GET'])
def get_managers(request):
    if request.method=='GET':
        try:
            managers=Manager.objects.all()
            serialize=ManagerGetSerializer(managers,many=True)
            return Response(serialize.data)
        except:
            return Response({'error': 'Managers not found'},status=status.HTTP_404_NOT_FOUND)
            
    
@api_view(['GET'])
def get_manager_by_id(request,id):
    if request.method=='GET':
        try:
            manager = Manager.objects.get(id=id)
            serializer = ManagerGetSerializer(manager)
            return Response(serializer.data)
        except:
            return Response({'error': 'Manager not found'},status=status.HTTP_404_NOT_FOUND)
         
         
@api_view(['POST'])
def create_manager(request):
    try:
        if request.method=="POST":
        
                data=request.data
                serialize=ManagerCreateSerializer(data=data)
                if serialize.is_valid():
                    serialize.save()    
                    return Response(serialize.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['PATCH'])   
def update_manager(request): 
    try:
        if request.method=="PATCH": 
            data=request.data
            try:
                obj=Manager.objects.get(id=data['id'])
                serialize=ManagerUpdateSerializer(obj,data=data,partial=True)
                if serialize.is_valid():
                    serialize.save()
                    return Response(serialize.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'error': 'Manager not found'},status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['DELETE'])
def Delete_manager(request,id):
    if request.method=="DELETE":
        try:
            obj=Manager.objects.get(id=id)
            obj.delete()
            return Response({"success":"Manager was deleted successfully"})
        except:
            return Response({'error': 'Manager not found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_employees(request):
    if request.method=='GET':
        try:
            obj=Employee.objects.all()
            serialize=EmployeeGetSerializer(obj,many=True)
            return Response(serialize.data)
        except:
            return Response({'error': 'employees not found'},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_employee_by_id(request,id):
    if request.method=='GET':
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeGetSerializer(employee)
            return Response(serializer.data)
        except:
            return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
         
         
@api_view(['POST'])
def create_employee(request):
    try:
        if request.method=="POST":
            data=request.data
            serialize=EmployeeCreateSerializer(data=data)
            if serialize.is_valid():
                serialize.save()    
                return Response(serialize.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def update_employee(request):
    try:
        data=request.data
        try:
            obj=Employee.objects.get(id=data['id'])
            serialize=EmployeeUpdateSerializer(obj,data=data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def Delete_employee(request,id):
    try:
        obj=Employee.objects.get(id=id)
        obj.delete()
        return Response({"success":"Employee was deleted successfully"})
    except:
        return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)

