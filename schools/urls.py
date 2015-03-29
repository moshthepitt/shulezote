from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from schools.views import SchoolView

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(SchoolView.as_view()), name='school'),
)
