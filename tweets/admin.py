from django.contrib import admin
from .models import Tweet, Tag

class TweetAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__', 'posted']


class TagAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__']
   


# Register your models here.
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Tag, TagAdmin)