from django.shortcuts import render, redirect
from django.template import Context
from .models import Article, Category
from .forms import CreateShareForm, ContactForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

shares = Article.objects.all()
categories = Category.objects.all()
tags = shares.values_list('tag', flat=True)

def home(request):

	context = {

		"shares": shares,
		"categories": categories,
		"rtags" : tags[:5],
	}

	return render(request, "home.html", context)

def profile(request):
	user = request.user
	form = CreateShareForm(request.POST or None)
	
	context = {
		"user": user,
		"form": form,
		"shares": shares.filter(user=user),
		
	
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		return redirect('/myprofile')

	return render(request, "profile.html", context)

def public(request, user): 	

	context = {

		"shares": shares.filter(user_id=User.objects.get(username=user)),
		"user": user,

	}

	return render(request, "public.html", context)

def view_tag(request, tag):
	
    context = {
    	'user': request.user,
        'tags': tags,
        'categories': categories,
        'shares': shares.filter(tag=tag),
        'tag': tag,
        }


    return render(request, "view_tag.html", context)  

def view_category(request, category):

	context = {
    	'user': request.user,
        'category': category,
        'categories': categories,
        'shares': shares.filter(category=categories.filter(category=category).values('id')),
         'tags': tags,
        }

	return render(request, "view_category.html", context)  


def contact(request):

	form = ContactForm(request.POST or None)
	context = {
		"form": form,

	}

	if form.is_valid():		
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_subject = form.cleaned_data.get('subject')
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
		if request.user:
			user = request.user
			html_message = """ <h3>From:%s</h3><br><p>%s</p> """%(user, form_message)
		else:
			user = form_email
			html_message = """ <h3>From: %s</h3><br><p>%s</p> """%(user, form_message)

		send_mail(form_subject,
				form_message,
				from_email,
				to_email,
				html_message = html_message,
				fail_silently=True)

		return redirect('/')
	

	return render(request, "contact.html", context)


def about(request):

	about = '''Article Share is designed to optimize your ability to catalog articles 
	through sharing with other users under tag names with comments regarding the articles shared.'''

	return render(request, "about.html", {"about": about,})















