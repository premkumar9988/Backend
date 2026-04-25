from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book,Cart,Order,User,OrderItem,Category,Payment
from .serializers import BookSerializer,CartSerializer,OrderSerializer,UserSerializer,OrderItemSerializer,CategorySerializer,PaymentSerializer 
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookListView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class CartListView(generics.ListCreateAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]    
    
class OrderListView(generics.ListCreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]    
    
class UserCreateView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer   
    
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer  
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer        
    
    
class PaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer     
    