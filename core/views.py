from django.views.generic.list import ListView
from django.conf import settings
from django.http import HttpResponse

from schools.models import School
from kcse.utils import get_last_year

ADS_TXT = getattr(settings, 'ADS_TEXT', '')


class HomePageView(ListView):
    model = School
    template_name = "home.html"

    def get_queryset(self):
        queryset = super(HomePageView, self).get_queryset().order_by('?')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['top_secondary_schools'] = School.objects.with_kcse(year=get_last_year())
        return context


def ads_txt_view(request):
    return HttpResponse(ADS_TXT)
