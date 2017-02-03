from django.shortcuts import render
from django.contrib.auth.models import *
from rest_framework import viewsets
from musical_api.serializers import *
# Create your views here.

class ArtistsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited.
    """
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializers


class AlbumsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializers

class GenresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited.
    """
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
    
class SongsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializers

class CustomersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializers
