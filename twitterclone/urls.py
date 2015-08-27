from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^myprofile/', 'tweets.views.profile', name='myprofile'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'tweets.views.home', name = 'home'),
    url(r'^contact$', 'tweets.views.contact', name='contact'),
    url(r'^about$', 'tweets.views.about', name='about'),
    url(r'^public/(?P<user>\w{0,30})/$', 'tweets.views.public', name='public'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/view/(?P<category>\w{0,20})/$', 'tweets.views.view_category', name='view_category'),
    url(r'^tag/view/(?P<tag>\w{0,30})/$', 'tweets.views.view_tag', name='view_tag'),
]
