from customers.models import Customer
from django.http import JsonResponse , Http404
from customers.serializers import CustomerSerializer,UserSerializer
from rest_framework.decorators import api_view , permission_classes #which methods are allowed
from rest_framework.response import Response #json 404 or html response
from rest_framework import status #options fro status code -->200s 300s  400s and others
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def customers(request):
    if request.method=='GET':
        #invoke serializer and return to client
        data = Customer.objects.all() # to get all our cutomer objects 
        # now serialize all this data
        serializer = CustomerSerializer(data , many=True)
        # return JsonResponse({'customers': serializer.data}) #serializer.data dar vaghe serialize shode ye data  hast- choon in ba json compatible hast va ma ino be onvan response miferestim
        return Response({'customers': serializer.data}) #serializer.data dar vaghe serialize shode ye data  hast- choon in ba json compatible hast va ma ino be onvan response miferestim
    elif request.method=='POST':
        serializer = CustomerSerializer(data=request.data) #in dg mesle paeen arg 1 nadare chun nemikhaym edit kunim balke mikhay ijad kunim
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST','DELETE']) #define api that can take get post delete request --> we used api decorator which describes functionality fro this function
@permission_classes([IsAuthenticated])
def customer(request,id):
    try:
        data = Customer.objects.get(pk=id) # we don't wanna get all of them so we use get() instead of all() 
    except Customer.DoesNotExist:
        #raise Http404('Customer does not exist') 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = CustomerSerializer(data)
        # return JsonResponse({'customer': serializer.data}) #serializer.data dar vaghe serialize shode ye data  hast- choon in ba json compatible hast va ma ino be onvan response miferestim
        return Response({'customer': serializer.data}) 
    elif request.method=='DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) #har status e ke fek mikuni monaseb hast ro bezar
    elif request.method=='POST':
        serializer = CustomerSerializer(data , data=request.data) #arg1 --> data ee ke az DB migiri hast va arg2 mishe new Data
        if serializer.is_valid(): #check to see if the serialization was valid
            serializer.save()
            return Response({'customer':serializer.data})

        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data= request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)