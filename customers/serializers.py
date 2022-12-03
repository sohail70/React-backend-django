from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer #model e ke mikhay serialize kunim
        fields = '__all__' #che field hayee tosh mikhaym? hame --> mishe har attribute ke mikhay ro to list bezari
        