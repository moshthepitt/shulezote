from django.conf.urls import patterns, url

from places.views import CountyView, ProvinceView, DistrictView, DivisionView
from places.views import LocationView, SubLocationView, SchoolZoneView, ConstituencyView

urlpatterns = patterns('',
    url(r'^county/(?P<slug>[\w-]+)/$', CountyView.as_view(), name='county'),
    url(r'^province/(?P<slug>[\w-]+)/$', ProvinceView.as_view(), name='province'),
    url(r'^district/(?P<province_slug>[\w-]+)/(?P<slug>[\w-]+)/$', DistrictView.as_view(), name='district'),
    url(r'^division/(?P<district_slug>[\w-]+)/(?P<slug>[\w-]+)/$', DivisionView.as_view(), name='division'),
    url(r'^location/(?P<division_slug>[\w-]+)/(?P<slug>[\w-]+)/$', LocationView.as_view(), name='location'),
    url(r'^sub-location/(?P<location_slug>[\w-]+)/(?P<slug>[\w-]+)/$', SubLocationView.as_view(), name='sub_location'),
    url(r'^school-zone/(?P<county_slug>[\w-]+)/(?P<slug>[\w-]+)/$', SchoolZoneView.as_view(), name='school_zone'),
    url(r'^constituency/(?P<county_slug>[\w-]+)/(?P<slug>[\w-]+)/$', ConstituencyView.as_view(), name='constituency'),
)
