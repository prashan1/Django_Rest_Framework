from rest_framework import serializers 
from .models import * 


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

    def validate_name(self,value):
        if value.split()[0].lower() == 'pankaj':
            raise serializers.ValidationError('No Losers are allowed')
        return value

    def validate_age(self,value):
        age = value
        if age > 25:
            raise serializers.ValidationError('Only Young BLood Are Allowed, YOU ARE OLD!. ')
        return value

    #First 100 students are allowed
    def validate(self,value):
        stu_count = StudentModel.objects.all().count()
        if stu_count > 100:
            raise serializers.ValidationError('All the seats are full, cannot accomodate more students')
        return value

    def update(self,instance, validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.age = validate_data.get('age',instance.age)
        instance.rollno = validate_data.get('rollno',instance.rollno)
        instance.save()
        return instance

    def post(self, validate_data):
        return StudentModel.create(**validate_data)
    class Meta:
        model=StudentModel
        fields ='__all__'