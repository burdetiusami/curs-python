from django.shortcuts import render
from .decorators import user_is_staff_or_manager
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'main/home.html')

@login_required
@user_is_staff_or_manager
def logged_home(request):
    return render(request, 'main/logged_home.html')

@login_required
@user_is_staff_or_manager
def employees_index(request):
    return render(request, 'main/employees_index.html')

@login_required
@user_is_staff_or_manager
def orders_index(request):
    return render(request, 'main/orders_index.html')

@login_required
@user_is_staff_or_manager
def fleet_index(request):
    return render(request, 'main/fleet_index.html')


