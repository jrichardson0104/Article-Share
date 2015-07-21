from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.db.models import permalink
# Create your models here.

class Tweet(models.Model):
	tweet = models.CharField(max_length=140, blank=False)
	user = models.ForeignKey(User, default=0)
	posted = models.DateField(auto_now_add=True, auto_now=False)
	tag = models.ManyToManyField('tweets.Tag')
	
	def __str__(self):
		return str(self.tweet)

class Tag(models.Model):
	tag = models.CharField(unique=True, max_length = 20)
	
	def __str__(self):
		return str(self.tag)


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	about = models.TextField(max_length=200)
	