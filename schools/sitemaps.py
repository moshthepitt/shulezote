from django.contrib.sitemaps import Sitemap
from schools.models import School


class SchoolSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return School.objects.all()

    def lastmod(self, obj):
        return obj.updated_on
