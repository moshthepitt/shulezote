from django.contrib.gis import admin

from schools.models import School


class SchoolAdmin(admin.GeoModelAdmin):
    search_fields = ['name']
    list_filter = ['level']

admin.site.register(School, SchoolAdmin)
