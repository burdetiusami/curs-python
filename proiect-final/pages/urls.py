from django.urls import path
from pages.views import home, users, orders

urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('orders/', orders, name='orders'),

]