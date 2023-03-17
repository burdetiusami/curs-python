from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from fleet.models import Trucks, Trailers
from django.contrib.auth.mixins import LoginRequiredMixin



# Trucks
class TrucksListView(ListView):
    model = Trucks
    template_name = 'trucks/trucks_list.html'

# Trailers
class TrailersListView(ListView):
    model = Trailers
    template_name = 'trailers/trailers_list.html'

# Trucks
class CreateTrucksView(LoginRequiredMixin, CreateView):
    model = Trucks
    template_name = 'trucks/trucks_form.html'
    fields = ['truck_make', 'truck_model', 'year', 'mileage', 'color', 'truck_image', 'status']

    def get_success_url(self):
        return reverse('fleet:trucks_list')

# Trailers   
class CreateTrailersView(LoginRequiredMixin, CreateView):
    model = Trailers
    template_name = 'trailers/trailers_form.html'
    fields = ['trailer_make', 'trailer_model', 'year', 'color', 'trailer_image', 'status']

    def get_success_url(self):
        return reverse('fleet:trailers_list')


# Trucks
class UpdateTrucksView(LoginRequiredMixin, UpdateView):
    model = Trucks
    fields = ['truck_make', 'truck_model', 'year', 'mileage', 'color', 'truck_image', 'status']
    template_name = 'trucks/trucks_form.html'

    def get_success_url(self):
        return reverse('fleet:trucks_list')

# Trailers    
class UpdateTrailersView(LoginRequiredMixin, UpdateView):
    model = Trailers
    fields = ['trailer_make', 'trailer_model', 'year', 'color', 'trailer_image', 'status']
    template_name = 'trailers/trailers_form.html'

    def get_success_url(self):
        return reverse('fleet:trailers_list')

# Trucks
@login_required
def deactivate_trucks(request, pk):
    Trucks.objects.filter(id=pk).update(status=False)

    return redirect('fleet:trucks_list')

# Trailers
@login_required
def deactivate_trailers(request, pk):
    Trailers.objects.filter(id=pk).update(status=False)

    return redirect('fleet:trailers_list')

# Trucks
@login_required
def activate_trucks(request, pk):
    Trucks.objects.filter(id=pk).update(status=True)

    return redirect('fleet:trucks_list')

# Trailers
@login_required
def activate_trailers(request, pk):
    Trailers.objects.filter(id=pk).update(status=True)

    return redirect('fleet:trailers_list')

# Trucks
class DeleteTrucksView(LoginRequiredMixin, DeleteView):
    model = Trucks
    template_name = 'trucks/on_delete_truck.html'

    def get_success_url(self):
        return reverse('fleet:trucks_list')

# Trailers
class DeleteTrailersView(LoginRequiredMixin, DeleteView):
    model = Trailers
    template_name = 'trailers/on_delete_trailer.html'

    def get_success_url(self):
        return reverse('fleet:trailers_list')