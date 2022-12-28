import graphene
from graphene_django import DjangoObjectType

from customers.models import Customer , Order
import time
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = '__all__'

class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        industry = graphene.String()

    customer = graphene.Field(CustomerType)

    def mutate(root , info , name , industry):
        time.sleep(5)
        # raise
        customer = Customer(name=name , industry=industry)
        customer.save()
        return CreateCustomer(customer = customer )

class CreateOrder(graphene.Mutation):
    class Arguments:
        description = graphene.String()
        total_in_cents = graphene.Int()
        customer = graphene.ID()
    
    order = graphene.Field(OrderType)
    
    def mutate(root , info , description , total_in_cents , customer):
        order = Order(description=description , total_in_cents=total_in_cents , customer_id=customer) # deghat kun agar customer_id ro benvisi customer dar graph ql moghe mutation query null mide --> chun it expects cutomer object not a number 
        order.save()
        return CreateOrder(order=order)


class Query(graphene.ObjectType):
    customers = graphene.List(CustomerType)
    orders = graphene.List(OrderType)
    customer_by_name = graphene.Field(CustomerType , name=graphene.String (required=True))
    # customer_by_name = graphene.List(CustomerType , name=graphene.String (required=True)) #age element haye tekrari dar data hat dari az Field nemsihe use kard bayad List bezari (yani age duplicate data age dari List bezan)

    def resolve_customers(root,info):
        return Customer.objects.all()

    def resolve_orders(root , info):
        return Order.objects.select_related('customer').all()

    def resolve_customer_by_name(root , info , name):
        try:
            return Customer.objects.filter(name=name).first()
            # return Customer.objects.get(name=name) #age mikkhay chandtasho begire
        except Customer.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    create_order = CreateOrder.Field()


schema = graphene.Schema(query=Query , mutation=Mutation) #schema dovomi ke dar setting.py neveshti dar GRAPHEN in object hast 