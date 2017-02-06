from django.db import models

# Create your models here.
class Artists(models.Model):
	"""Artists model class
		The purpose of this class is to define the Artists data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by FirstName)
	"""
	
	First_Name = models.CharField(max_length=100, blank=True, default='')
	Last_Name = models.CharField(max_length=100, blank=True, default='')
	Age = models.IntegerField()
	Band_Name = models.CharField(max_length=100, null=True)
	Bio = models.TextField()

	class Meta:
		ordering = ('First_Name',)

	def __str__(self):
		return '{} {} {} {} {}'.format(self.First_Name, self.Last_Name, self.Age, self.Band_Name, self.Bio)

class Genres(models.Model):
	"""Genres model class
		The purpose of this class is to define the Genres data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by GenreName)
	"""
	Genre_Name = models.CharField(max_length=100, blank=True, default='')

	class Meta:
		ordering = ('Genre_Name',)

	def __str__(self):
		return '{}'.format(self.Genre_Name,)

class Albums(models.Model):
	"""Albums model class
		The purpose of this class is to define the Albums data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by AlbumTitle)
	"""
	Album_Title = models.CharField(max_length=100, blank=True, default='')
	Release_Date = models.DateTimeField(null=True, blank=True)
	Album_Description = models.TextField()
	Number_of_Sales = models.IntegerField()
	Artist = models.ForeignKey(Artists, null=True)

	class Meta:
		ordering = ('Album_Title',)


	def __str__(self):
		return '{} {} {} {} {}'.format(self.Album_Title, self.Release_Date, self.Album_Description, self.Number_of_Sales, self.Artist,)


class Songs(models.Model):
	"""Songs model class
		The purpose of this class is to define the Songs data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by SongTitle)
	"""
	Song_Title = models.CharField(max_length=100, blank=True, default='')
	Duration = models.DurationField()
	Genre = models.ForeignKey(Genres, null=True)
	Album = models.ForeignKey(Albums, null=True)
	Artist = models.ForeignKey(Artists, null=True)

	class Meta:
		ordering = ('Song_Title',)
	   
	def __str__(self):
		return '{} {} {} {} {}'.format(self.Song_Title, self.Duration, self.Genre, self.Album, self.Artist,)






class Customers(models.Model):
	"""Customers model class
		The purpose of this class is to define the Customers data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by email)
	"""
	First_Name = models.CharField(max_length=100, blank=True, default='')
	Last_Name = models.CharField(max_length=100, blank=True, default='')
	Email = models.EmailField()
	Joined = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ('Email',)

	def __str__(self):
		return '{} {} {} {}'.format(self.First_Name, self.Last_Name, self.Email, self.Joined,)


