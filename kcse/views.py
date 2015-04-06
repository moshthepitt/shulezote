from django.contrib.contenttypes.models import ContentType
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.http import Http404

from schools.models import School
from kcse.utils import get_last_year


class AllSchoolsView(ListView):
    model = School
    template_name = "kcse/all_schools.html"

    def get_queryset(self):
        queryset = School.objects.with_kcse(year=self.year, ordered=False)
        if self.sort:
            queryset = queryset.order_by(self.sort, 'name')
        else:
            queryset = queryset.order_by('-kcse_mean', '-A', '-kcse_students', 'name')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllSchoolsView, self).get_context_data(**kwargs)
        context['current_page'] = self.request.GET.get('page')
        context['year'] = self.year
        context['sort'] = self.sort
        context['sort_asc'] = True
        return context

    def dispatch(self, *args, **kwargs):
        possible_sorting = ['kcse_mean', 'kcse_students', 'A', '-kcse_mean', '-kcse_students', '-A']

        if self.request.GET.get('year') and self.request.GET.get('year').isdigit():
            self.year = int(self.request.GET.get('year'))
        else:
            self.year = get_last_year()

        self.sort_asc = True
        if self.request.GET.get('sort') and self.request.GET.get('sort') in possible_sorting:
            self.sort = self.request.GET.get('sort')
            if self.sort[0] == '-':
                self.sort_asc = False
        else:
            self.sort = None
        return super(AllSchoolsView, self).dispatch(*args, **kwargs)


class LocationView(ListView):
    model = School
    template_name = "kcse/places.html"

    def get_queryset(self):
        queryset = School.objects.with_kcse(year=self.year, ordered=False)
        if self.object.meta().model_name == "county":
            queryset = queryset.filter(county=self.object)
        elif self.object.meta().model_name == "province":
            queryset = queryset.filter(province=self.object)
        elif self.object.meta().model_name == "district":
            queryset = queryset.filter(district=self.object)
        elif self.object.meta().model_name == "division":
            queryset = queryset.filter(division=self.object)
        elif self.object.meta().model_name == "location":
            queryset = queryset.filter(location=self.object)
        elif self.object.meta().model_name == "sublocation":
            queryset = queryset.filter(sub_location=self.object)
        elif self.object.meta().model_name == "schoolzone":
            queryset = queryset.filter(school_zone=self.object)
        elif self.object.meta().model_name == "constituency":
            queryset = queryset.filter(constituency=self.object)

        if self.sort:
            queryset = queryset.order_by(self.sort, 'name')
        else:
            queryset = queryset.order_by('-kcse_mean', '-A', '-kcse_students', 'name')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['current_page'] = self.request.GET.get('page')
        context['year'] = self.year
        context['sort'] = self.sort
        context['sort_asc'] = True
        context['object'] = self.object
        return context

    def dispatch(self, *args, **kwargs):
        location_type = get_object_or_404(ContentType, app_label='places', model=kwargs['model_name'])
        try:
            location = location_type.get_object_for_this_type(pk=kwargs['pk'])
            self.object = location
        except:
            raise Http404

        possible_sorting = ['kcse_mean', 'kcse_students', 'A', '-kcse_mean', '-kcse_students', '-A']

        if self.request.GET.get('year') and self.request.GET.get('year').isdigit():
            self.year = int(self.request.GET.get('year'))
        else:
            self.year = get_last_year()

        self.sort_asc = True
        if self.request.GET.get('sort') and self.request.GET.get('sort') in possible_sorting:
            self.sort = self.request.GET.get('sort')
            if self.sort[0] == '-':
                self.sort_asc = False
        else:
            self.sort = None
        return super(LocationView, self).dispatch(*args, **kwargs)
