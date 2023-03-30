from django.urls import path
from apps.orders import views
from main.views import orders_index

app_name = 'orders'

urlpatterns = [
    path('orders/', orders_index, name='orders_index'),
    
    path('orders-list/', views.OrdersListView.as_view(), name='orders_list'),
    path('create/', views.CreateOrdersView.as_view(), name='create_order'),
    path('<int:pk>/update/', views.UpdateOrdersView.as_view(), name='modify'),
    path('<int:pk>/deactivate/', views.deactivate_orders, name='deactivate'),
    path('<int:pk>/activate/', views.activate_orders, name='activate'),
    path('<int:pk>/delete/', views.DeleteOrdersView.as_view(), name='delete'),
]
