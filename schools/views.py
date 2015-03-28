from django.views.generic.detail import DetailView

from schools.models import School


class SchoolView(DetailView):
    model = School
    template_name = "schools/school.html"

    def get_context_data(self, **kwargs):
        context = super(SchoolView, self).get_context_data(**kwargs)
        return context
