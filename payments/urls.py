# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', views.item_view, name='item'),
    path('create-payment-intent/<int:id>/', views.create_payment_intent, name='create_payment_intent'),


    path('item/<int:id>/', views.item_view),
    path('buy/<int:id>/', views.buy_item),
    path('order/<int:id>/', views.order_view),
    path('buy_order/<int:id>/', views.buy_order),
]