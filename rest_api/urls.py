from django.urls import path
from .views import *

urlpatterns = [
    path('manager_getall', get_managers, name='get_managers'),
    path('manager_get/<str:id>', get_manager_by_id, name='get_manager_by_id'),
    path('manager_get_employee/<str:id>', get_employees_by_manager, name='get_manager_by_id'),
    path('manager_create', create_manager, name='create_manager'),
    path('manager_update', update_manager, name='update_manager'),
    path('manager_delete/<str:id>', Delete_manager, name='delete_manager'),
    path('employee_getall', get_employees, name='get_employees'),
    path('employee_get/<str:id>', get_employee_by_id, name='get_employee_by_id'),
    path('employee_create', create_employee, name='create_employee'),
    path('employee_update', update_employee, name='update_employee'),
    path('employee_delete/<str:id>', Delete_employee, name='delete_employee'),
]