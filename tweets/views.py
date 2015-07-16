from django.shortcuts import render
from django.template import Context
from .models import Tweet, Tag
# Create your views here.

def home(request):

	tweets = Tweet.objects.all()
	tags = Tag.objects.all()

	# t = Tweet.objects.get(id=1)
	# print(t.tag.all())


	context = {

		"tweets": tweets,
		"tags": tags,
	}

	return render(request, "home.html", context)

