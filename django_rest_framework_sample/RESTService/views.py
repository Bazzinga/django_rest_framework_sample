from rest_framework import generics
from .serializers import RestaurantSerializer
from django_rest_framework_sample.models import Restaurant


class RestaurantList(generics.ListAPIView):
    """
    API endpoint that represents a list of restaurants
    """
    model = Restaurant
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a single restauran.
    """
    model = Restaurant
    serializer_class = RestaurantSerializer

            