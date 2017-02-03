from rest_framework import serializers
from musical_api.models import *

class AlbumsSerializers(serializers.HyperlinkedModelSerializer):
	"""
	purpose: convert complex data into native python datatypes for JSON rendering
	author: Zach
	methods and subclasses: meta
	model: Albums from models.py
	fields: all fields form Albums data model are included
	"""

	class Meta:
		model = Albums
		fields = ('url', 'id','AlbumTitle', 'ReleaseDate', 'AlbumDescription', 'NumberofSales', 'ArtistId',)

class SongsSerializers(serializers.HyperlinkedModelSerializer):
	"""
	purpose: convert complex data into native python datatypes for JSON rendering
	author: Zach
	methods and subclasses: meta
	model: Songs from models.py
	fields: all fields form Songs data model are included
	"""

	class Meta:
		model = Songs
		fields = ('url','id', 'SongTitle', 'Duration', 'GenreId', 'AlbumId', 'ArtistId',)

class ArtistsSerializers(serializers.HyperlinkedModelSerializer):
	"""
	purpose: convert complex data into native python datatypes for JSON rendering
	author: Zach
	methods and subclasses: meta
	model: Albums from models.py
	fields: all fields form Albums data model are included
	"""

	class Meta:
		model = Artists
		fields = ('url','id', 'FirstName', 'LastName', 'BandName', 'Age', 'Bio',)

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
		fields = ('url','id','GenreName',)

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
		fields = ('url','id', 'FirstName', 'LastName', 'Email', 'Joined',)
