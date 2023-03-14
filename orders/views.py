from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from orders.models import Orders
from django.contrib.auth.mixins import LoginRequiredMixin


# Orders views

class OrdersListView(ListView):
    model = Orders
    template_name = 'orders/orders_list.html'


class CreateOrdersView(LoginRequiredMixin, CreateView):
    model = Orders
    template_name = 'orders/orders_form.html'
    fields = ['company', 'address', 'cargo_info', 'eta', 'status']

    def get_success_url(self):
        return reverse('orders:orders_list')


class UpdateOrdersView(LoginRequiredMixin, UpdateView):
    model = Orders
    fields = ['company', 'address', 'cargo_info', 'eta', 'status']
    template_name = 'orders/orders_form.html'

    def get_success_url(self):
        return reverse('orders:orders_list')


@login_required
def deactivate_orders(request, pk):
    Orders.objects.filter(id=pk).update(status=False)

    return redirect('orders:orders_list')


@login_required
def activate_orders(request, pk):
    Orders.objects.filter(id=pk).update(status=True)

    return redirect('orders:orders_list')


class DeleteOrdersView(LoginRequiredMixin, DeleteView):
    model = Orders
    template_name = 'orders/on_delete.html'

    def get_success_url(self):
        return reverse('orders:orders_list')
