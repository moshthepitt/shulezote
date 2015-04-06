from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from kcse.views import AllSchoolsView

urlpatterns = patterns('',
    url(r'^$', cache_page(60 * 60 * 24)(AllSchoolsView.as_view()), name='all_schools'),
)
