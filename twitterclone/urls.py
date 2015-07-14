from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'twitterclone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'tweets.views.home', name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
]
