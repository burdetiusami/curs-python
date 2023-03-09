from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def users(request):
    return render(request, 'pages/users.html')

def orders(request):
    return render(request, 'pages/orders.html')