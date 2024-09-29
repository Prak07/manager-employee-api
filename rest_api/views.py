from django.shortcuts import render

# Create your views here.
from .models import Manager, Employee
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import uuid
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='get',operation_description="Retrieve list of all employees")
@api_view(['GET'])
def get_managers(request):
    if request.method=='GET':
        try:
            managers=Manager.objects.all()
            serialize=ManagerGetSerializer(managers,many=True)
            return Response(serialize.data)
        except:
            return Response({'error': 'Managers not found'},status=status.HTTP_404_NOT_FOUND)
            
@swagger_auto_schema(method='get', operation_description="Retrieve a specific manager's details by their unique ID")    
@api_view(['GET'])
def get_manager_by_id(request,id):
    if request.method=='GET':
        try:
            manager = Manager.objects.get(id=id)
            serializer = ManagerGetSerializer(manager)
            return Response(serializer.data)
        except:
            return Response({'error': 'Manager not found'},status=status.HTTP_404_NOT_FOUND)
         
@swagger_auto_schema(method='post', operation_description='''Create a new manager in the organization.Example parameters 
                        
    {
        "name": "Amit Sharma",
        "age": 40,
        "email": "amit.sharma@example.com",
        "date_joined": "2022-01-15",
        "department": "Sales"
    }''',request_body=ManagerCreateSerializer)         
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
            
@swagger_auto_schema(method='patch', operation_description='''Update an existing manager's information by ID.Used Patch request to update part of an existing resource. It allows sending only the fields that need to be updated, without affecting the others.Example Parametes:
                     
    {
        "id":1,
        "age":20
    }''',request_body=ManagerUpdateSerializer)
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

@swagger_auto_schema(method='delete', operation_description="Delete a manager by their unique ID.")
@api_view(['DELETE'])
def Delete_manager(request,id):
    if request.method=="DELETE":
        try:
            obj=Manager.objects.get(id=id)
            obj.delete()
            return Response({"success":"Manager was deleted successfully"})
        except:
            return Response({'error': 'Manager not found'},status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='get', operation_description="Retrieve list of all employees in the organization.")
@api_view(['GET'])
def get_employees(request):
    if request.method=='GET':
        try:
            obj=Employee.objects.all()
            serialize=EmployeeGetSerializer(obj,many=True)
            return Response(serialize.data)
        except:
            return Response({'error': 'employees not found'},status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='get', operation_description="Retrieve a specific employee's details by their unique ID.")    
@api_view(['GET'])
def get_employee_by_id(request,id):
    if request.method=='GET':
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeGetSerializer(employee)
            return Response(serializer.data)
        except:
            return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
         
@swagger_auto_schema(method='post', operation_description='''Create a new employee in the organization.If the manager given is not present in the organization then it will raise a 400 Bad request Error.Example Parameters     
    
    {
        "name": "Aakash Desai",
        "age": 28,
        "email": "aakash.desai@example.com",
        "date_joined": "2023-01-10",
        "designation": "Software Engineer",
        "manager": 2
    }''',request_body=EmployeeCreateSerializer)
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

@swagger_auto_schema(method='patch', operation_description='''Update an existing employee's information by ID.Used Patch request to update part of an existing resource. It allows sending only the fields that need to be updated, without affecting the others.Example Parametes:
                     
    {
        "id":10,
        "age":20
    }''',request_body=EmployeeUpdateSerializer)    
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

@swagger_auto_schema(method='delete', operation_description="Delete an employee by their unique ID")
@api_view(['DELETE'])
def Delete_employee(request,id):
    try:
        obj=Employee.objects.get(id=id)
        obj.delete()
        return Response({"success":"Employee was deleted successfully"})
    except:
        return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='get', operation_description="Retrieve a list of employees assigned to a specific manager by manager ID.This Api can be used to get list of all employees under one manager")
@api_view(['GET'])
def get_employees_by_manager(request,id):
    if request.method=='GET':
        try:
            manager = Manager.objects.get(id=id)
            try:
                employee = Employee.objects.filter(manager=id)
                serializer = EmployeeGetSerializer(employee,many=True)
                return Response(serializer.data)
            except:
                return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error': 'Manager not found'},status=status.HTTP_404_NOT_FOUND)
         