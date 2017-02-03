from django.db import models

# Create your models here.
class Albums(models.Model):
	"""Albums model class
		The purpose of this class is to define the Albums data model.
		author: Zachary 
		methods: __str__ Returns a string
		subclasses: Meta (with ordering by last_name)
	"""
    AlbumTitle = models.CharField(max_length=100, blank=True, default='')
    ReleaseDate = models.DateTimeField(null=True, blank=True)
    ALbumDescription = models.TextField()
    NumberofSales = models.IntegerField()
    ArtistId = models.ForeignKey(Artists, null=True)

    class Meta:
        ordering = ('AlbumTitle',)


    def __str__(self):
		return '{} {} {} {} {}'.format(self.AlbumTitle, self.ReleaseDate, self.ALbumDescription, self.NumberofSales, self.ArtistId)


class Songs(models.Model):
    SongTitle = models.CharField(max_length=100, blank=True, default='')
    Duration = models.DurationField()
    GenreId = models.ForeignKey(Genres, null=True)
    AlbumId = models.ForeignKey(Albums, null=True)
    ArtistId = models.ForeignKey(Artists, null=True)

    class Meta:
        ordering = ('SongTitle',)
       
    def __str__(self):
        return '{} {} {} {} {}'.format(self.SongTitle, self.Duration, self.GenreId, self.AlbumId, self.ArtistId)


class Artists(models.Model):
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
	GenreName = models.CharField(max_length=100, blank=True, default='')

	class Meta:
		ordering = ('GenreName')

    def __str__(self):
        return '{} {} {} {} {}'.format(self.GenreName)



class Customer(models.Model):
	FirstName = models.CharField(max_length=100, blank=True, default='')
	LastName = models.CharField(max_length=100, blank=True, default='')
	Email = models.EmailField()
    Joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
    	ordering = ('Email')

    def __str__(self):
        return '{} {} {} {}'.format(self.FirstName, self.LastName, self.Email, self.Joined)


