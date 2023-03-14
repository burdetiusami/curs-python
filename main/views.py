from django.shortcuts import render

def homepage(request):
    return render(request, 'main/home.html')

def employees(request):
    return render(request, 'main/employees.html')

def orders(request):
    return render(request, 'main/orders.html')

def logged_home(request):
    return render(request, 'main/logged_home.html')