from django.urls import path
from . import views

urlpatterns = [

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('purchase_confirmation/', views.purchase_confirmation, name='purchase_confirmation'),
    path('purchase_success/', views.purchase_success, name='purchase_success'),
    path('purchase_history/', views.purchase_history, name='purchase_history'),
    

]

