from django.views.generic.list import ListView

from schools.models import School
from kcse.views import get_last_year


class AllSchoolsView(ListView):
    model = School
    template_name = "kcse/all_schools.html"

    def get_context_data(self, **kwargs):
        context = super(AllSchoolsView, self).get_context_data(**kwargs)
        return context
