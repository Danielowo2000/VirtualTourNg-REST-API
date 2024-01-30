# Importing the necessary dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drfapp.models import Location
from drfapp.serializers import *
from rest_framework import generics, status
from rest_framework.generics import UpdateAPIView

# View that returns all locations
class LocationList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# View for each location detail
class LocationDetail(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        # Retrieve the location based on the location_id from the URL
        location_id = self.kwargs['location_id']
        return Location.objects.get(pk=location_id)

        
# view to create a new location
class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Location created", "data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
    
# update an existing location.
class LocationUpdate(generics.UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'  # Set the lookup field explicitly
    
    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({"detail": "Location updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": f"Error updating location: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
# Delete an existing location.
class LocationDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Location successfully deleted"}, status=status.HTTP_204_NO_CONTENT)   

# View that returns all tours
class TourList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Tour.objects.all()
    serializer_class = TourSerializer 

# View that retrieve each tour detail
class TourDetail(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        # Retrieve the location based on the location_id from the URL
        tour_id = self.kwargs['tour_id']
        return Tour.objects.get(pk=tour_id)
    
# view to create a new tour
class TourCreate(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Tour created", "data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

# update an existing Tour.
class TourUpdate(generics.UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'  # Set the lookup field explicitly
    
    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({"detail": "Location updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": f"Error updating : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
class TourDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        tour = self.get_object()
        tour.delete()
        return Response({"detail": "Tour deleted successfully."}, status=status.HTTP_204_NO_CONTENT)