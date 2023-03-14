from django.contrib import admin
from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('orders-list/', views.OrdersListView.as_view(), name='orders_list'),
    path('create/', views.CreateOrdersView.as_view(), name='create_order'),
    path('<int:pk>/update/', views.UpdateOrdersView.as_view(), name='modify'),
    path('<int:pk>/deactivate/', views.deactivate_orders, name='deactivate'),
    path('<int:pk>/activate/', views.activate_orders, name='activate'),
    path('<int:pk>/delete/', views.DeleteOrdersView.as_view(), name='delete'),
]
