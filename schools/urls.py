from django.conf.urls import url
from django.views.decorators.cache import cache_page

from schools.views import SchoolView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/amp$', cache_page(60 * 60 * 24)
        (SchoolView.as_view(template_name="schools/school.amp.html")), name='school_amp'),
    url(r'^(?P<slug>[\w-]+)/$', cache_page(60 * 60 * 24)(SchoolView.as_view()), name='school'),
]
