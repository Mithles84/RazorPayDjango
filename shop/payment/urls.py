from django.urls import path
from . import views

urlpatterns = [
    path('buy/', views.buy_tea, name='buy_tea'),
    path('success/', views.payment_success, name='payment_success'),
]
