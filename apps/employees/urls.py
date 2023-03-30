from django.urls import path
from apps.employees import views
from main.views import employees_index

app_name = 'employees'

urlpatterns = [
    path('employees/', employees_index, name='employees_index'),

    path('table/', views.employee_table, name='employee_table'),
    path('add/', views.CreateEmployeesView.as_view(), name='add_employee'),
    path('<int:pk>/update/', views.UpdateEmployeesView.as_view(), name='modify'),
    path('<int:pk>/deactivate/', views.deactivate_Employees, name='deactivate'),
    path('<int:pk>/activate/', views.activate_Employees, name='activate'),
    path('<int:pk>/delete/', views.delete_employee, name='delete'),
]