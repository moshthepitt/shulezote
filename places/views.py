from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from places.models import Province, County, District, Division, Location, SubLocation
from places.models import Constituency, SchoolZone
from schools.models import School


class CountyView(DetailView):
    model = County
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(CountyView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(county=self.object)
        context['current_page'] = self.request.GET.get('page')
        return context


class ProvinceView(DetailView):
    model = Province
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(ProvinceView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(province=self.object)
        context['current_page'] = self.request.GET.get('page')
        return context


class DistrictView(TemplateView):
    model = District
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(DistrictView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(district=self.object)
        context['object'] = self.object
        context['current_page'] = self.request.GET.get('page')
        return context

    def dispatch(self, *args, **kwargs):
        self.object = get_object_or_404(District, province__slug=kwargs['province_slug'], slug=kwargs['slug'])
        return super(DistrictView, self).dispatch(*args, **kwargs)


class DivisionView(TemplateView):
    model = Division
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(DivisionView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(division=self.object)
        context['object'] = self.object
        context['current_page'] = self.request.GET.get('page')
        return context

    def dispatch(self, *args, **kwargs):
        self.object = get_object_or_404(Division, district__slug=kwargs['district_slug'], slug=kwargs['slug'])
        return super(DivisionView, self).dispatch(*args, **kwargs)


class LocationView(TemplateView):
    model = Location
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(location=self.object)
        context['object'] = self.object
        context['current_page'] = self.request.GET.get('page')
        return context

    def dispatch(self, *args, **kwargs):
        self.object = get_object_or_404(Location, division__slug=kwargs['division_slug'], slug=kwargs['slug'])
        return super(LocationView, self).dispatch(*args, **kwargs)


class SubLocationView(TemplateView):
    model = SubLocation
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(SubLocationView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(sub_location=self.object)
        context['object'] = self.object
        context['current_page'] = self.request.GET.get('page')
        return context

    def dispatch(self, *args, **kwargs):
        self.object = get_object_or_404(SubLocation, location__slug=kwargs['location_slug'], slug=kwargs['slug'])
        return super(SubLocationView, self).dispatch(*args, **kwargs)


class SchoolZoneView(TemplateView):
    model = SchoolZone
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(SchoolZoneView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(school_zone=self.object)
        context['object'] = self.object
        context['current_page'] = self.request.GET.get('page')
        return context

    def dispatch(self, *args, **kwargs):
        self.object = get_object_or_404(SchoolZone, county__slug=kwargs['county_slug'], slug=kwargs['slug'])
        return super(SchoolZoneView, self).dispatch(*args, **kwargs)


class ConstituencyView(TemplateView):
    model = Constituency
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(ConstituencyView, self).get_context_data(**kwargs)
        context['school_list'] = School.objects.filter(constituency=self.object)
        context['object'] = self.object
        context['current_page'] = self.request.GET.get('page')
        return context

    def dispatch(self, *args, **kwargs):
        self.object = get_object_or_404(Constituency, county__slug=kwargs['county_slug'], slug=kwargs['slug'])
        return super(ConstituencyView, self).dispatch(*args, **kwargs)
