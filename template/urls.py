from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from core.views import HomePageView
from core.sitemaps import sitemaps

sitemap_urls = patterns('',
    (r'^sitemap\.xml$', 'fastsitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'fastsitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^place/', include('places.urls', namespace="place")),
    url(r'^school/', include('schools.urls', namespace="school")),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^page/', include('django.contrib.flatpages.urls')),
    url(r'^search/', include('haystack.urls')),
)

urlpatterns = urlpatterns + sitemap_urls

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
