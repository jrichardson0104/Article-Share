from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'twitterclone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^profile/', 'tweets.views.profile', name='profile'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'tweets.views.home', name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tags/view/(?P<tag>\w{0,20})/$', 'tweets.views.view_tag', name='view_tag'),
]
