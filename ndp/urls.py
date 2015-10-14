from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'ndp.views.home', name='home'),
    url(r'^about$', 'ndp.views.about', name='about'),
    url(r'^sector/(?P<slug>[\w-]+)$', 'ndp.views.sector', name='sector'),
    url(r'^organisation/(?P<org_id>\d+)$', 'ndp.views.organisation', name='organisation'),

    url(r'^admin/', include(admin.site.urls)),
)
