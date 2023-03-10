from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from orders.models import Orders


class OrdersListView(ListView):
    model = Orders
    template_name = 'orders/orders_list.html'


class CreateOrdersView(CreateView):
    model = Orders
    template_name = 'orders/orders_form.html'
    fields = ['company', 'address', 'cargo_info', 'eta', 'status']

    def get_success_url(self):
        return reverse('orders:orders_list')

class UpdateOrdersView(UpdateView):
    model = Orders
    fields = ['company', 'address', 'cargo_info', 'eta', 'status']
    template_name = 'orders/orders_form.html'

    def get_success_url(self):
        return reverse('orders:orders_list')
    

def deactivate_orders(request, pk):
    Orders.objects.filter(id=pk).update(status=False)

    return redirect('orders:orders_list')

def activate_orders(request, pk):
    Orders.objects.filter(id=pk).update(status=True)

    return redirect('orders:orders_list')

class DeleteOrdersView(DeleteView):
    model = Orders
    template_name = 'orders/on_delete.html'
    
    def get_success_url(self):
        return reverse('orders:orders_list')
