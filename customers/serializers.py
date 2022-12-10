from rest_framework import serializers
from customers.models import Customer
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer #model e ke mikhay serialize kunim
        fields = '__all__' #che field hayee tosh mikhaym? hame --> mishe har attribute ke mikhay ro to list bezari
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
    def create(self , validated_data): #we invoke this when we create a user object
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user