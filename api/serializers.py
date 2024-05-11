from rest_framework.serializers import *
from apps.models import *
from geopy.distance import distance


class CategorySerializer(ModelSerializer):
    products = SerializerMethodField('get_query')
    class Meta:
        model = Categories
        fields = ['id', 'name', 'products']


    def get_query(self, id):
        items = Products.objects.filter(category_id=id)
        serializer = ProductSerializer(instance=items, many=True)
        return serializer.data


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class FastFoodsSerializer(ModelSerializer):
    class Meta:
        model = Fastfoods
        fields = '__all__'

class OrdersSerializer(ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'
        depth = 2



class OrderItemsSerializer(ModelSerializer):
    total_money = SerializerMethodField('get_total', read_only=True)
    delivery_time_in_address = SerializerMethodField('get_time', read_only=True)
    class Meta:
        model = Order_items
        fields = '__all__'


    def get_total(self, obj):
        if obj.product_id.discount:
            total = int(obj.product_id.price*discount/100)*int(obj.quantity)
        else:
            total = int(obj.product_id.price)*int(obj.quantity)
        return total

    def get_time(self, obj):
        if (obj.quantity%4)==0:
            total_time = obj.quantity//4*5
        else:
            total_time = (obj.quantity//4+1)*5
        distanc = distance((obj.order_id.latitude, obj.order_id.longitude),
                           (obj.order_id.fastfood_id.latitude, obj.order_id.fastfood_id.longitude)).kilometers

        time = distanc*3+total_time
        if time%1==0:
            return time
        else:
            return int(time//1+1)
