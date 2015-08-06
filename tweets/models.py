from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
# Create your models here.

class Article(models.Model):
	share = models.CharField(max_length=140, blank=False)
	user = models.ForeignKey(User, default=0)
	posted = models.DateField(auto_now_add=True, auto_now=False)
	category = models.ManyToManyField('tweets.Category')
	tag = models.CharField(max_length=30, blank=True)
	url = models.URLField()

	def __str__(self):
		return str(self.share)

	class Meta:
		ordering = ['posted']

class Category(models.Model):
	category = models.CharField(unique=True, max_length = 20)
	
	def __str__(self):
		return str(self.category)

	class Meta:
		ordering = ['category']


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	about = models.TextField(max_length=200)
	