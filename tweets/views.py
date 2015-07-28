from django.shortcuts import render, redirect
from django.template import Context
from .models import Tweet, Tag
from .forms import CreateTweetForm, CreateTagForm
from django.contrib.auth.models import User
# Create your views hereself.
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
	tagform = CreateTagForm()
	form = CreateTweetForm()
	
	
	context = {
		"user": user,
		"form": form,
		"tweets": Tweet.objects.filter(user=user).all(),
		"tagform": tagform,
	
	}

	return render(request, "profile.html", context)

def add_tag(request):
	tagform = CreateTagForm(data=request.POST)
	if tagform.is_valid():
		
		tagform.save()
		
	else:

		tagform = CreateTagForm()
	return redirect('/profile')

def add_tweet(request):
	form = CreateTweetForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
	else:
		form = CreateTweetForm()
	return redirect('/profile')


def public(request, user):
	user = User.objects.filter(username=user)

	tweets = Tweet.objects.filter(user=user)

	context = {

		"tweets": tweets,
		"user": user,

	}

	return render(request, "public.html", context)



# def add_tag(request):
# 	form = CreateTagForm(request.POST or None)

# 	context = {
		
# 		"form": form,
	
		
# 	}

# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return redirect('/profile')

# 	return render(request, "add_tag.html", context)

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