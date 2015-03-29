from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.core.paginator import Paginator

from schools.models import School


class SchoolSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return School.objects.all()

    def lastmod(self, obj):
        return obj.updated_on


def school_sitemaps(chunk=2000):
    """
    next we'll attemtp to generate a number of sitemaps in chunks using Paginator and GenericSitemap
    """
    school_sitemap = {}
    schools = School.objects.all()
    paginated_schools = Paginator(schools, chunk)
    for this_page in paginated_schools.page_range:
        school_dict = {
            'queryset': paginated_schools.page(this_page).object_list,
            'date_field': 'updated_on',
        }
        school_sitemap['schools_%s' % this_page] = GenericSitemap(school_dict, priority=0.6, changefreq='monthly')
    return school_sitemap
