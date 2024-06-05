from rest_framework import serializers
from api.models import Student

#Validators

def start_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name should be satrt with A')

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100, validators=[start_with_a])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)


#create 
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
#update
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #Field Level Validation

    def validate_roll(self,value):   #roll me jo input krnge whi value aayega
        if value >=200:
            raise serializers.ValidationError("Seat full")
        return value
    
    #object level Validation

    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() =='aryan' and ct.lower() !='ballia':
            raise serializers.ValidationError("city must be ballia")
        return data
        