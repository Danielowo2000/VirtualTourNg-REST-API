from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    # Requirement for django rest framework.
    path('api-auth/', include('rest_framework.urls')),
    # Endpoint for extracting user token (POST REQUEST) user credentials
    # Functionality: Obtain API-Token for authentication.
    # Security Requirements: NO token authentication required.
    path('api/token/', obtain_auth_token, name ='obtain'), 
    # Endpoint for obtaining all Tourism locations (GET REQUEST).
    # Functionality: Retrieve all locations.
    # Security Requirements: NO token authentication required.
    path('api/locations/', LocationList.as_view(), name ='location-list'),
    # Functionality: Retrieve details of a specific location (GET REQUEST)
    # Security Requirements: NO token authentication required.
    path('api/locations/<int:location_id>/', LocationDetail.as_view(), name='location-detail'),
    # Functionality: Create a new location (POST REQUEST).
    # Security Requirements: token authentication required.
    path('api/locations/create/', LocationCreate.as_view(), name='location-create'),
    # Functionality: Update details of a specific location (PUT REQUEST).
    # Security Requirements: JWT token authentication required.
    path('api/update-locations/<int:pk>/', LocationUpdate.as_view(), name='location-update'),
    # Functionality: Delete details of a specific location (DELETE REQUEST).
    # Security Requirements: JWT token authentication required.
    path('api/delete-location/<int:pk>/', LocationDelete.as_view(), name='location-delete'),
    # Functionality: Retrieve all tours (GET REQUEST).
    # Security Requirements: No JWT token authentication required.
    path('api/tours/', TourList.as_view(), name='tour-list'),
    # Functionality: Retrieve details of a specific tour (GET REQUEST).
    # Security Requirements: No JWT token authentication required.
    path('api/tours/<int:tour_id>/', TourDetail.as_view(), name='tour-list'),
    # Functionality: Create a new tour (POST REQUEST).
    # Security Requirements: JWT token authentication required.
    path('api/create-tours/', TourCreate.as_view(), name='tour-create'),
    # Functionality: Update details of a specific tour.
    # Security Requirements: JWT token authentication required.
    path('api/update-tour/<int:pk>/', TourUpdate.as_view(), name='tour-update'),
    # Functionality: Delete a specific tour.
    # Security Requirements: JWT token authentication required.
    path('api/delete-tour/<int:pk>/', TourDelete.as_view(), name='tour-update'),

]
