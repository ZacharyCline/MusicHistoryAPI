from rest_framework import serializers
from music_api.models import *

class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
	"""
    purpose: convert complex data into native python datatypes for JSON rendering
    author: Zach
    methods and subclasses: meta
    model: Albums from models.py
    fields: all fields form Albums data model are included
    """

    class Meta:
    	model = Albums
    	fields = '__all__'

class SongsSerializer(serializers.HyperlinkedModelSerializer):
	"""
    purpose: convert complex data into native python datatypes for JSON rendering
    author: Zach
    methods and subclasses: meta
    model: Songs from models.py
    fields: all fields form Songs data model are included
    """

    class Meta:
    	model = Songs
    	fields = '__all__'

class ArtistsSerializers(serializers.HyperlinkedModelSerializer):
	"""
    purpose: convert complex data into native python datatypes for JSON rendering
    author: Zach
    methods and subclasses: meta
    model: Albums from models.py
    fields: all fields form Albums data model are included
    """

    class Meta:
        model = Songs
        fields = '__all__'

class GenresSerializers(serializers.HyperlinkedModelSerializer):
    '''
    purpose: convert complex data into native python datatypes for JSON rendering
    author: Zach
    methods and subclasses: meta
    model: Albums from models.py
    fields: all fields form Genres data model are included
    '''
    class Meta: 
        model = Genres
        fields = '__all__'

class CustomersSerializers(serializers.HyperlinkedModelSerializer):
    '''
    purpose: convert complex data into native python datatypes for JSON rendering
    author: Zach
    methods and subclasses: meta
    model: Customers from models.py
    fields: all fields form Customers data model are included
    '''
    class Meta:
        model = Customers
        fields = '__all__'
