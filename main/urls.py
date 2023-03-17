from django.contrib import admin
from django.urls import path
from main.views import homepage, employees, orders, logged_home, fleet_index

app_name = 'main'

urlpatterns = [
    path('', homepage, name='home'),
    path('employees/', employees, name='employees'),
    path('orders/', orders, name='orders'),
    path('home/', logged_home, name='logged-home'),
    path('fleet/', fleet_index , name='fleet_index'),
]