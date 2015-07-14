from django.db import models
# from users.models import Users
# Create your models here.
class Tweet(models.Model):
	tweet = models.CharField(max_length=140, blank=False)
	# user = models.ForeignKey('Users.user')
	posted = models.DateField(auto_now_add=True, auto_now=False)
	tag = models.ForeignKey('tweets.Tag')
	
	def __str__(self):
		return str(self.tweet)

class Tag(models.Model):
	tag = models.CharField(unique=True, max_length = 20)

	def __str__(self):
		return str(self.tag)



