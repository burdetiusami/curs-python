from django.urls import path
from employees import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeesView.as_view(), name='employees_list'),
    path('add/', views.CreateEmployeesView.as_view(), name='add_employee'),
    path('<int:pk>/update/', views.UpdateEmployeesView.as_view(), name='modify'),
    path('<int:pk>/deactivate/', views.deactivate_Employees, name='deactivate'),
    path('<int:pk>/activate/', views.activate_Employees, name='activate'),
    path('<int:pk>/delete/', views.DeleteEmployeesView.as_view(), name='delete'),
]