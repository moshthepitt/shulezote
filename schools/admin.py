# from django.contrib import admin
from django.contrib.gis import admin

from schools.models import School

class SchoolAdmin(admin.GeoModelAdmin):
    pass

admin.site.register(School,SchoolAdmin)
