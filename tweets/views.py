from django.shortcuts import render, redirect
from django.template import Context
from .models import Article, Category
from .forms import CreateShareForm, ContactForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


def home(request):

	shares = Article.objects.all()[:15]
	categories = Category.objects.all()
	rtags = Article.objects.values_list('tag', flat=True)[:5]
	

	context = {

		"shares": shares,
		"categories": categories,
		"rtags" : rtags,
	}

	return render(request, "home.html", context)

def profile(request):
	
	user = request.user

	form = CreateShareForm(request.POST or None)
	
	
	context = {
		"user": user,
		"form": form,
		"shares": Article.objects.filter(user=user),
		
	
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		return redirect('/myprofile')

	return render(request, "profile.html", context)

def public(request, user):

	userid = User.objects.filter(username=user)
	shares = Article.objects.filter(user=userid)	

	context = {

		"shares": shares,
		"user": user,

	}

	return render(request, "public.html", context)

def view_tag(request, tag):
	
    categories = Category.objects.all()
    shares = Article.objects.filter(tag=tag)
    tags = Article.objects.values_list('tag', flat=True)
    context = {
    	'user': request.user,
        'tag': tag,
        'categories': categories,
        'shares': shares,
        'tags': tags,
        }


    return render(request, "view_tag.html", context)  

def view_category(request, category):
	
    category = Category.objects.get(category=category)
    categories = Category.objects.all()
    shares = Article.objects.filter(category=category)
    tags = Article.objects.values_list('tag', flat=True)

    context = {
    	'user': request.user,
        'category': category,
        'categories': categories,
        'shares': shares,
         'tags': tags,
        }


    return render(request, "view_category.html", context)  


def contact(request):

	form = ContactForm(request.POST or None)
	context = {
		"form": form,

	}

	if form.is_valid():
		#print (form.cleaned_data)
		
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

	return render(request, "about.html", {})















