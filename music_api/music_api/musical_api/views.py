from django.shortcuts import render
from django.contrib.auth.models import *
from rest_framework import viewsets
from music_api.musical_api.serializers import *
# Create your views here.

class ArtistsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerialzer


class AlbumsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

class GenresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    
class SongsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializers

class CustomersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
