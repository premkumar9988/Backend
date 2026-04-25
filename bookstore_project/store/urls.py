from django.urls import path
from .views import *
from .views import RegisterView,UserList,CategoryList, OrderItemList,PaymentView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='create-user'),
    path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),

    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('cart/', CartListView.as_view()),
    path('cart/<int:pk>/', CartDetailView.as_view()),
    path('orders/', OrderListView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
    path('orderitems/', OrderItemList.as_view(), name='order-items'),
    path('category/', CategoryList.as_view(), name='category'), 
    path('user/', UserList.as_view(), name='user-list'), 
    path("payments/", PaymentView.as_view()),
    path("payments/<int:pk>/", PaymentView.as_view()),
     path('books/', BookListView.as_view(), name='books'),
     path('api/payment/', PaymentView.as_view(), name='payment'),
]