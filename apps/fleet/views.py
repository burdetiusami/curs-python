from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.fleet.models import Trucks, Trailers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



# Trucks
class TrucksListView(LoginRequiredMixin,ListView):
    model = Trucks
    template_name = 'fleet/trucks/trucks_list.html'

# Trailers
class TrailersListView(LoginRequiredMixin,ListView):
    model = Trailers
    template_name = 'fleet/trailers/trailers_list.html'

# Trucks
class CreateTrucksView(LoginRequiredMixin, CreateView):
    model = Trucks
    template_name = 'fleet/trucks/trucks_form.html'
    fields = ['truck_make', 'truck_model', 'year', 'mileage', 'color', 'registration_plate', 'truck_image', 'status']

    def get_success_url(self):
        messages.success(self.request, f'the truck {self.object.registration_plate} has been successfully created!')
        return reverse('fleet:trucks_list')

# Trailers   
class CreateTrailersView(LoginRequiredMixin, CreateView):
    model = Trailers
    template_name = 'fleet/trailers/trailers_form.html'
    fields = ['trailer_make', 'trailer_model', 'year', 'color', 'registration_plate', 'trailer_image', 'status']

    def get_success_url(self):
        messages.success(self.request, f'the trailer {self.object.registration_plate} has been successfully created!')
        return reverse('fleet:trailers_list')


# Trucks
class UpdateTrucksView(LoginRequiredMixin, UpdateView):
    model = Trucks
    fields = ['truck_make', 'truck_model', 'year', 'mileage', 'color', 'registration_plate', 'truck_image', 'status']
    template_name = 'fleet/trucks/trucks_form.html'

    def get_success_url(self):
        messages.success(self.request, f'the truck {self.object.registration_plate} has been successfully updated!')
        return reverse('fleet:trucks_list')

# Trailers    
class UpdateTrailersView(LoginRequiredMixin, UpdateView):
    model = Trailers
    fields = ['trailer_make', 'trailer_model', 'year', 'color', 'registration_plate', 'trailer_image', 'status']
    template_name = 'fleet/trailers/trailers_form.html'

    def get_success_url(self):
        messages.success(self.request, f'the trailer {self.object.registration_plate} has been successfully updated!')
        return reverse('fleet:trailers_list')

# Trucks
@login_required
def deactivate_trucks(request, pk):
    Trucks.objects.filter(id=pk).update(status=False)
    truck = Trucks.objects.get(id=pk)
    truck.save()
    messages.warning(request, f'the truck {truck.registration_plate} is now non-operational!')
    return redirect('fleet:trucks_list')

# Trailers
@login_required
def deactivate_trailers(request, pk):
    Trailers.objects.filter(id=pk).update(status=False)
    trailer = Trailers.objects.get(id=pk)
    trailer.save()
    messages.warning(request, f'the trailer {trailer.registration_plate} is now non-operational!')
    return redirect('fleet:trailers_list')

# Trucks
@login_required
def activate_trucks(request, pk):
    Trucks.objects.filter(id=pk).update(status=True)
    truck = Trucks.objects.get(id=pk)
    truck.save()
    messages.success(request, f'the truck {truck.registration_plate} is now operational!')
    return redirect('fleet:trucks_list')

# Trailers
@login_required
def activate_trailers(request, pk):
    Trailers.objects.filter(id=pk).update(status=True)
    trailer = Trailers.objects.get(id=pk)
    trailer.save()
    messages.success(request, f'the trailer {trailer.registration_plate} is now operational!')
    return redirect('fleet:trailers_list')

# Trucks
class DeleteTrucksView(LoginRequiredMixin, DeleteView):
    model = Trucks
    template_name = 'fleet/trucks/on_delete_truck.html'

    def get_success_url(self):
        messages.warning(self.request, f'the truck {self.object.registration_plate} has been permanently deleted!')
        return reverse('fleet:trucks_list')

# Trailers
class DeleteTrailersView(LoginRequiredMixin, DeleteView):
    model = Trailers
    template_name = 'fleet/trailers/on_delete_trailer.html'

    def get_success_url(self):
        messages.warning(self.request, f'the trailer {self.object.registration_plate} has been permanently deleted!')
        return reverse('fleet:trailers_list')