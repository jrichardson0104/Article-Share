from django import forms

from tweets.models import Article, Category, UserProfile


class CreateShareForm(forms.ModelForm):
	share = forms.CharField(required=True, max_length = 140, widget=forms.Textarea(attrs={'style': 'height: 4em;', 'placeholder': 'Add a quick comment about the url'}))
	tag = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Please use only numbers and letters'}))

	class Meta:
		model = Article
		fields =['category', 'share', 'url', 'tag']
		exclude = ('user',)

	def clean_tag(self):
		tag = str(self.cleaned_data.get('tag')).strip()
		if tag.isalnum():
			return tag
		else:
			raise forms.ValidationError("Please use only letters and numbers")
		return tag

class CreateCategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['category']


class ContactForm(forms.Form):
	email = forms.EmailField()
	subject = forms.CharField(max_length = 30)
	message = forms.CharField(max_length = 1000, widget=forms.Textarea())
	








