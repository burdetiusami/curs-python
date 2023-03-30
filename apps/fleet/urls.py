from django.urls import path
from apps.fleet import views
from main.views import fleet_index


app_name = 'fleet'

urlpatterns = [
    path('fleet/', fleet_index, name='fleet_index'),

    path('truck-list/', views.TrucksListView.as_view(), name='trucks_list'),
    path('create-truck/', views.CreateTrucksView.as_view(), name='create_truck'),
    path('<int:pk>/update-truck/', views.UpdateTrucksView.as_view(), name='modify-truck'),
    path('<int:pk>/deactivate-truck/', views.deactivate_trucks, name='deactivate-truck'),
    path('<int:pk>/activate-truck/', views.activate_trucks, name='activate-truck'),
    path('<int:pk>/delete-truck/', views.DeleteTrucksView.as_view(), name='delete-truck'),

    path('trailer-list/', views.TrailersListView.as_view(), name='trailers_list'),
    path('create-trailer/', views.CreateTrailersView.as_view(), name='create_trailer'),
    path('<int:pk>/update-trailer/', views.UpdateTrailersView.as_view(), name='modify-trailer'),
    path('<int:pk>/deactivate-trailer/', views.deactivate_trailers, name='deactivate-trailer'),
    path('<int:pk>/activate-trailer/', views.activate_trailers, name='activate-trailer'),
    path('<int:pk>/delete-trailer/', views.DeleteTrailersView.as_view(), name='delete-trailer'),
]