"""
URL configuration for manager_employee_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Manager_Employee_api",
        default_version='v1',
        description="""The Employee Management API enables organizations to efficiently manage employees and their respective managers.
        
    This API provides functionality to create, retrieve, update, and delete employee records, allowing employees to select their managers
    to employees and perform various operations on employee data.
    
    There are two models manager and eployee connected with many to one field using manager as the foriegnkey in the employee table.
    
    Key Features:
    - Add new employees or managers with relevant details.
    - Assign managers to employees or update their managers.
    - Retrieve a list of all employees or managers, or filter by specific criteria.
    - Update or remove employee or manager records from the system.
    - If a manager is deleted that is assigned to employees then the manager column of employee is set to null so that a new manager can be assigned.
    
    No authentication is required for this API.
    
    """,
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('rest_api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
