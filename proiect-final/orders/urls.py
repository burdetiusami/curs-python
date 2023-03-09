from django.contrib import admin
from django.urls import path
from users import views

app_name = 'orders'

urlpatterns = [
    path('', views.UsersView.as_view(), name='orders_index'),


]
