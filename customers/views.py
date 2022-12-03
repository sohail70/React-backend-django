from customers.models import Customer
from django.http import JsonResponse , Http404
from customers.serializers import CustomerSerializer

def customers(request):
    #invoke serializer and return to client
    data = Customer.objects.all() # to get all our cutomer objects 
    # now serialize all this data
    serializer = CustomerSerializer(data , many=True)
    return JsonResponse({'customers': serializer.data}) #serializer.data dar vaghe serialize shode ye data  hast- choon in ba json compatible hast va ma ino be onvan response miferestim

def customer(request,id):
    try:
        data = Customer.objects.get(pk=id) # we don't wanna get all of them so we use get() instead of all() 
    except Customer.DoesNotExist:
        raise Http404('Customer does not exist') 

    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data}) #serializer.data dar vaghe serialize shode ye data  hast- choon in ba json compatible hast va ma ino be onvan response miferestim
