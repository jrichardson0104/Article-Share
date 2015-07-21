from django.shortcuts import render, redirect
from django.template import Context
from .models import Tweet, Tag
from .forms import CreateTweetForm
# Create your views here.
from django.contrib.auth.models import User
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

def profile(request):
	
	user = request.user
	form = CreateTweetForm(request.POST or None)
	context = {
		"user": user,
		"form": form,
		"tweets": Tweet.objects.filter(user=user).all(),
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		



	return render(request, "profile.html", context)


# def add_tag(request, tag):
# 	form = CreateTagForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 	return redirect('/profile')

def view_tag(request, tag):

    tag = Tag.objects.get(tag=tag)
    tags = Tag.objects.all()
    tweets = Tweet.objects.filter(tag=tag).all()

    context = {
    	'user': request.user,
        'tag': tag,
        'tags': tags,
        'tweets': tweets,
        }


    return render(request, "view_tag.html", context)  