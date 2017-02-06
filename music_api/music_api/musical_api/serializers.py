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
		fields = ('url', 'id','Album_Title', 'Release_Date', 'Album_Description', 'Number_of_Sales', 'Artist',)

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
		fields = ('url','id', 'Song_Title', 'Duration', 'Genre', 'Album', 'Artist',)

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
		fields = ('url','id', 'First_Name', 'Last_Name', 'Band_Name', 'Age', 'Bio',)

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
		fields = ('url','id','Genre_Name',)

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
		fields = ('url','id', 'First_Name', 'Last_Name', 'Email', 'Joined',)
