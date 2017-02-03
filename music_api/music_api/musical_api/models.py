from django.db import models

# Create your models here.
class Artists(models.Model):
	"""Artists model class
		The purpose of this class is to define the Artists data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by FirstName)
	"""
	
	FirstName = models.CharField(max_length=100, blank=True, default='')
	LastName = models.CharField(max_length=100, blank=True, default='')
	Age = models.IntegerField()
	BandName = models.CharField(max_length=100, null=True)
	Bio = models.TextField()

	class Meta:
		ordering = ('FirstName',)

	def __str__(self):
		return '{} {} {} {} {}'.format(self.FirstName, self.LastName, self.Age, self.BandName, self.Bio)

class Genres(models.Model):
	"""Genres model class
		The purpose of this class is to define the Genres data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by GenreName)
	"""
	GenreName = models.CharField(max_length=100, blank=True, default='')

	class Meta:
		ordering = ('GenreName',)

	def __str__(self):
		return '{}'.format(self.GenreName,)

class Albums(models.Model):
	"""Albums model class
		The purpose of this class is to define the Albums data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by AlbumTitle)
	"""
	AlbumTitle = models.CharField(max_length=100, blank=True, default='')
	ReleaseDate = models.DateTimeField(null=True, blank=True)
	AlbumDescription = models.TextField()
	NumberofSales = models.IntegerField()
	ArtistId = models.ForeignKey(Artists, null=True)

	class Meta:
		ordering = ('AlbumTitle',)


	def __str__(self):
		return '{} {} {} {} {}'.format(self.AlbumTitle, self.ReleaseDate, self.ALbumDescription, self.NumberofSales, self.ArtistId,)


class Songs(models.Model):
	"""Songs model class
		The purpose of this class is to define the Songs data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by SongTitle)
	"""
	SongTitle = models.CharField(max_length=100, blank=True, default='')
	Duration = models.DurationField()
	GenreId = models.ForeignKey(Genres, null=True)
	AlbumId = models.ForeignKey(Albums, null=True)
	ArtistId = models.ForeignKey(Artists, null=True)

	class Meta:
		ordering = ('SongTitle',)
	   
	def __str__(self):
		return '{} {} {} {} {}'.format(self.SongTitle, self.Duration, self.GenreId, self.AlbumId, self.ArtistId,)






class Customers(models.Model):
	"""Customers model class
		The purpose of this class is to define the Customers data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by email)
	"""
	FirstName = models.CharField(max_length=100, blank=True, default='')
	LastName = models.CharField(max_length=100, blank=True, default='')
	Email = models.EmailField()
	Joined = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ('Email',)

	def __str__(self):
		return '{} {} {} {}'.format(self.FirstName, self.LastName, self.Email, self.Joined,)


