from django.conf.urls import patterns, url

from schools.views import SchoolView

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', SchoolView.as_view(), name='school'),
)
