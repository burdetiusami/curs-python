from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.models import Users

# CreateView -> adaugarea datelor in baza de date (instante noi)
# DetailView -> vizualizarea datelor unei instante din baza de date (furnizez pk(primary key))
# ListView ->   vizualizarea datelor a mai multor instante din baza de date
# UpdateView -> modificarea datelor din baza de date (furnizez pk)
# DeleteView -> stergerea datelor din baza de date


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'

class CreateUsersView(CreateView):
    model = Users
    template_name = 'users/users_form.html'
    fields = ['first_name', 'last_name', 'user_name', 'user_email', 'user_password']

    def get_success_url(self):
        return reverse('users:users_list')
    
class UpdateUsersView(UpdateView):
    model = Users
    fields = ['first_name', 'last_name', 'user_name', 'user_email', 'user_password']
    template_name = 'users/users_form.html'

    def get_success_url(self):
        return reverse('users:users_list')
    

def deactivate_users(request, pk):
    Users.objects.filter(id=pk).update(active=False)

    return redirect('users:users_list')

def activate_users(request, pk):
    Users.objects.filter(id=pk).update(active=True)

    return redirect('users:users_list')

class DeleteUsersView(DeleteView):
    model = Users
    template_name = 'users/on_delete.html'
    
    def get_success_url(self):
        return reverse('users:users_list')
    
