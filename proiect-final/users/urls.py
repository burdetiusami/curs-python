from django.contrib import admin
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('users-list', views.UsersListView.as_view(), name='users_list'),
    path('add/', views.CreateUsersView.as_view(), name='add_user'),
    path('<int:pk>/update/', views.UpdateUsersView.as_view(), name='modify'),
    path('<int:pk>/deactivate/', views.deactivate_users, name='deactivate'),
    path('<int:pk>/activate/', views.activate_users, name='activate'),
    path('<int:pk>/delete/', views.DeleteUsersView.as_view(), name='delete'),
    

]
