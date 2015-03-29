from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from places.views import CountyView, ProvinceView, DistrictView, DivisionView
from places.views import LocationView, SubLocationView, SchoolZoneView, ConstituencyView

urlpatterns = patterns('',
    url(r'^county/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(CountyView.as_view()), name='county'),
    url(r'^province/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(ProvinceView.as_view()), name='province'),
    url(r'^district/(?P<province_slug>[\w-]+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(DistrictView.as_view()), name='district'),
    url(r'^division/(?P<district_slug>[\w-]+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(DivisionView.as_view()), name='division'),
    url(r'^location/(?P<division_slug>[\w-]+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(LocationView.as_view()), name='location'),
    url(r'^sub-location/(?P<location_slug>[\w-]+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(SubLocationView.as_view()), name='sub_location'),
    url(r'^school-zone/(?P<county_slug>[\w-]+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(SchoolZoneView.as_view()), name='school_zone'),
    url(r'^constituency/(?P<county_slug>[\w-]+)/(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(ConstituencyView.as_view()), name='constituency'),
)
