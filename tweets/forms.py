from django import forms
from tweets.models import Article, Category, UserProfile
from django.core.validators import URLValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineCheckboxes

class CreateShareForm(forms.ModelForm):
	
	share = forms.CharField(required=True, label="", max_length = 140, widget=forms.Textarea(attrs={'style': 'height: 4em;', 'placeholder': 'Add a Quick Comment for Your Article'}))
	tag = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={'placeholder': 'Enter a Tag for Your Share'}))
	category = forms.ModelMultipleChoiceField(required=True, label="", widget=forms.CheckboxSelectMultiple(attrs={'body': 'padding-left: 70px;'}), queryset=Category.objects.all())
	url = forms.URLField(required = True, label="", widget=forms.URLInput( attrs={'placeholder': 'Article URL'}))
	
	helper = FormHelper()
	helper.layout = Layout(InlineCheckboxes('category'))

	class Meta:
		model = Article
		fields =['category', 'share', 'url', 'tag']
	

	def clean_tag(self):
		tag = str(self.cleaned_data.get('tag')).strip()
		if tag.isalnum():
			return tag
		else:
			raise forms.ValidationError("Please use only letters and numbers and no spaces.")
		return tag


class ContactForm(forms.Form):
	email = forms.EmailField()
	subject = forms.CharField(max_length = 30)
	message = forms.CharField(max_length = 1000, widget=forms.Textarea())
	








