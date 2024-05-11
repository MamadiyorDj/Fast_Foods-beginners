from django.shortcuts import render
from .serializers import *
from apps.models import *
from rest_framework.views import APIView, Response
from rest_framework.generics import *
from rest_framework.permissions import *
from .permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.


# class CategoryListApiView(APIView):
#     def get(self, request):
#         categories = Categories.objects.all()
#         serializers = CategoryApi(categories, many=True)
#         return Response(serializers.data)
class UsersListAPIView(ListAPIView):
    permission_classes = [IsUserInSuperuser,]
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UsersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserInSuperuser,]
    queryset = Users
    serializer_class = UserSerializer

class CategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Categories
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    permission_classes = [IsUserInSuperuser,]
    queryset = Categories
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserInSuperuser,]
    queryset = Categories
    serializer_class = CategorySerializer


class ProductListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Products
    serializer_class = ProductSerializer

class ProductCreateAPIView(CreateAPIView):
    permission_classes = (IsUserInOfitsiant,)
    queryset = Products
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserInOfitsiant,)
    queryset = Products
    serializer_class = ProductSerializer


class FastFoodsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Fastfoods.objects.all()
    serializer_class = FastFoodsSerializer

class FastFoodDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Fastfoods
    serializer_class = FastFoodsSerializer

class FastFoodCreateAPIView(CreateAPIView):
    permission_classes = [IsUserInSuperuser,]
    queryset = Fastfoods
    serializer_class = FastFoodsSerializer


class FastfoodRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserInSuperuser,]
    queryset = Fastfoods
    serializer_class = FastFoodsSerializer


class OrdersListAPIView(ListAPIView):
    permission_classes = [IsUserInUser,]
    # queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def get_queryset(self):
        if self.request.user.user_role == "S" or self.request.user.user_role == "O":
            return Orders.objects.all()
        elif self.request.user.user_role == "U":
            f=self.request.user
            return Orders.objects.filter(user_id=f)
        else:
            return False

class OrderDetailAPIView(RetrieveAPIView):
    permission_classes = [IsUserInUser]
    # queryset = Orders
    serializer_class = OrdersSerializer

    def get_queryset(self):
        if self.request.user.user_role == "S" or self.request.user.user_role == "O":
            return Orders.objects.all()
        elif self.request.user.user_role == "U":
            f = self.request.user
            return Orders.objects.filter(user_id=f)
        else:
            return False

class OrderCreateAPIView(CreateAPIView):
    permission_classes = [IsUserInUser]
    queryset = Orders
    serializer_class = OrdersSerializer


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserInUser]
    # queryset = Orders
    serializer_class = OrdersSerializer

    def get_queryset(self):
        if self.request.user.user_role == "S" or self.request.user.user_role == "O":
            return Orders.objects.all()
        elif self.request.user.user_role == "U":
            f = self.request.user
            return Orders.objects.filter(user_id=f)
        else:
            return False


class OrderItemsListAPIView(ListAPIView):
    permission_classes = [IsUserInUser]
    # queryset = Order_items.objects.all()
    serializer_class = OrderItemsSerializer

    def get_queryset(self):
        if self.request.user.user_role == "S" or self.request.user.user_role == "O":
            return Order_items.objects.all()
        elif self.request.user.user_role == "U":
            f = self.request.user
            for emp in Orders.objects.filter(user_id=f):
                queryset = Order_items.objects.filter(order_id=emp).order_by('-pk')
                return queryset

        else:
            return False


class OrderItemDetailAPIView(RetrieveAPIView):
    permission_classes = [IsUserInUser]
    # queryset = Order_items
    serializer_class = OrderItemsSerializer

    def get_queryset(self):
        if self.request.user.user_role == "S" or self.request.user.user_role == "O":
            return Order_items.objects.all()
        elif self.request.user.user_role == "U":
            f = self.request.user
            for emp in Orders.objects.filter(user_id=f):
                queryset = Order_items.objects.filter(order_id=emp).order_by('-pk')
                return queryset

        else:
            return False

class OrderItemCreateAPIView(CreateAPIView):
    permission_classes = [IsUserInUser]
    queryset = Order_items
    serializer_class = OrderItemsSerializer

class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserInUser]
    # queryset = Order_items
    serializer_class = OrderItemsSerializer

    def get_queryset(self):
        if self.request.user.user_role == "S" or self.request.user.user_role == "O":
            return Order_items.objects.all()
        elif self.request.user.user_role == "U":
            f = self.request.user
            for emp in Orders.objects.filter(user_id=f):
                queryset = Order_items.objects.filter(order_id=emp).order_by('-pk')
                return queryset

        else:
            return False









