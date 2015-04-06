from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from kcse.views import AllSchoolsView, LocationView

urlpatterns = patterns('',
    url(r'^$', cache_page(60 * 60 * 24)(AllSchoolsView.as_view()), name='all_schools'),
    url(r'^place/(?P<model_name>[\w-]+)/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(LocationView.as_view()), name='location'),
)
