from django.db import models

# Create your models here.

class Nominee(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	number_noms = models.IntegerField(default=0)
	winner = models.ForeignKey(Nominee, related_name='+', default=0) # added related name because there was a clash between this and noms... TBD
	noms = models.ManyToManyField(Nominee, through='Nomination')

	def __unicode__(self):
		return self.name

class Nomination(models.Model):
	nominee = models.ForeignKey(Nominee)
	category = models.ForeignKey(Category)
	votes = models.IntegerField(default=0)