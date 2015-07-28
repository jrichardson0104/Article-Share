from django import forms
from tweets.models import Tweet, Tag, UserProfile
from django.forms import ComboField



class CreateTweetForm(forms.ModelForm):

	class Meta:
		model = Tweet
		exclude = ('user',)


class CreateTagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ['tag']







