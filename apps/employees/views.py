from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from apps.users.models import CustomUser


@login_required
def employee_table(request):
    employees = CustomUser.objects.filter(is_employee=True)
    context = {'employees': employees}
    return render(request, 'employees/employee_table.html', context)


class CreateEmployeesView(LoginRequiredMixin, CreateView):
    model = CustomUser
    employees = CustomUser.objects.filter(is_employee=True)
    context = {'employees': employees}

    template_name = 'employees/employees_form.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'active']

    def get_success_url(self):
        messages.success(self.request, f'the employee {self.object.first_name} {self.object.last_name} has been successfully created!')
        return reverse('employees:employees_list')


class UpdateEmployeesView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    employees = CustomUser.objects.filter(is_employee=True)
    context = {'employees': employees}
    template_name = 'users/register_employee.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'is_active']
    
    def get_success_url(self):
        messages.success(self.request, f'the employee {self.object.first_name} {self.object.last_name} has been successfully edited!')
        return reverse('employees:employee_table')

@login_required
def deactivate_Employees(request, pk):
    CustomUser.objects.filter(id=pk, is_employee=True).update(is_active=False)
    employee = CustomUser.objects.get(id=pk)
    employee.save()
    messages.warning(request, f'the employee {employee.first_name} {employee.last_name} has been deactivated!')
    return redirect('employees:employee_table')

@login_required
def activate_Employees(request, pk):
    CustomUser.objects.filter(id=pk, is_employee=True).update(is_active=True)
    employee = CustomUser.objects.get(id=pk)
    employee.save()
    messages.success(request, f'the employee {employee.first_name} {employee.last_name} has been activated!')
    return redirect('employees:employee_table')

@login_required
def delete_employee(request, pk):
    employee = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employee_table')
    context = {'employee': employee}
    return render(request, 'employees/on_delete_employee.html', context)