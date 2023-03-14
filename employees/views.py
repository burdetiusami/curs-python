from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from employees.models import Employees

class EmployeesView(LoginRequiredMixin, ListView):
    model = Employees
    template = 'employees/employees_list.html'


class CreateEmployeesView(LoginRequiredMixin, CreateView):
    model = Employees
    template_name = 'employees/employees_form.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'active']

    def get_success_url(self):
        return reverse('employees:employees_list')


class UpdateEmployeesView(LoginRequiredMixin, UpdateView):
    model = Employees
    fields = ['first_name', 'last_name', 'username', 'email', 'active']
    template_name = 'employees/employees_form.html'
    def get_success_url(self):
        return reverse('employees:employees_list')

@login_required
def deactivate_Employees(request, pk):
    Employees.objects.filter(id=pk).update(active=False)

    return redirect('employees:employees_list')

@login_required
def activate_Employees(request, pk):
    Employees.objects.filter(id=pk).update(active=True)

    return redirect('employees:employees_list')


class DeleteEmployeesView(LoginRequiredMixin, DeleteView):
    model = Employees
    template_name = 'employees/on_delete_employee.html'

    def get_success_url(self):
        return reverse('employees:employees_list')