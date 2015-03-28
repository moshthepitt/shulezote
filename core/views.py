from django.views.generic.list import ListView

from schools.models import School


class HomePageView(ListView):
    model = School
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
