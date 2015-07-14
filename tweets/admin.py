from django.contrib import admin
from .models import Tweet, Tag

class TweetAdmin(admin.ModelAdmin):
	display_list = ["__str__", "tag", "posted"]


class TagAdmin(admin.ModelAdmin):

    # for tag in Tags:
    #     count = Tweets.objects.filter(tag=tag).count()
    #     tweetcount[Tags.tag] = count
    #     print(tweetcount)
    display_list = ["__str__"]


# Register your models here.
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Tag, TagAdmin)