from rest_framework import serializers
from .models import Manager,Employee

class ManagerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        exclude=['id','createdat','updatedat']
        
    def validate(self, data):
        special_characters="!@#$%^&*()-+?_=,<>/0123456789"
        if any (c in special_characters for c in data[ 'name']) :
            raise serializers. ValidationError('Name cannot contain special characters')
        return data
    
class ManagerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        exclude=['createdat','updatedat']
          
    def validate(self, data):
        if 'name' in data:
            special_characters="!@#$%^&*()-+?_=,<>/0123456789"
            if any (c in special_characters for c in data[ 'name']) :
                raise serializers. ValidationError('Name cannot contain special characters')
        return data

class ManagerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields="__all__"
        
        
    
class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        exclude=['id','createdat','updatedat']

    def validate(self, data):
        special_characters="!@#$%^&*()-+?_=,<>/0123456789"
        if any (c in special_characters for c in data['name']):
            raise serializers. ValidationError('Name cannot contain special characters')
        
        return data
    
    def validate_manager(self, data):
        try:
            id=data.id
            manager = Manager.objects.get(id=id)
        except Manager.DoesNotExist:
            raise serializers.ValidationError('Manager with this unique ID does not exist.')
        return manager
    
class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        exclude=['createdat','updatedat']


    def validate(self, data):
        if 'name' in data:
            special_characters="!@#$%^&*()-+?_=,<>/0123456789"
            if any (c in special_characters for c in data[ 'name']) :
                raise serializers. ValidationError('Name cannot contain special characters')    
        return data
    
    def validate_manager(self, data):
        try:
            manager = Manager.objects.get(id=data.id)
        except Manager.DoesNotExist:
            raise serializers.ValidationError('Manager with this unique ID does not exist.')
        return manager
    
class EmployeeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"