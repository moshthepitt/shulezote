from django.views.generic.list import ListView

from schools.models import School
from kcse.utils import get_last_year


class AllSchoolsView(ListView):
    model = School
    template_name = "kcse/all_schools.html"

    def get_queryset(self):
        queryset = School.objects.with_kcse(year=self.year)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllSchoolsView, self).get_context_data(**kwargs)
        context['current_page'] = self.request.GET.get('page')
        context['year'] = self.year
        return context

    def dispatch(self, *args, **kwargs):
        if self.request.GET.get('year') and self.request.GET.get('year').isdigit():
            self.year = int(self.request.GET.get('year'))
        else:
            self.year = get_last_year()
        return super(AllSchoolsView, self).dispatch(*args, **kwargs)
