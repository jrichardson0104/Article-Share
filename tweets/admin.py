from django.contrib import admin
from .models import Tweet, Tag

class TweetAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__','get_tags', 'posted', 'user']
	class Meta:
		model = Tweet
	def get_tags(self, obj):
		return "\n".join([tweet.tag for tweet in obj.tag.all()])


class TagAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__']
	


# Register your models here.
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Tag, TagAdmin)