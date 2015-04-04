from django.contrib import admin

from places.models import County, Constituency, Province, District
from places.models import Division, Location, SubLocation, SchoolZone


class CountyAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ['name']


class DistrictAdmin(admin.ModelAdmin):
    search_fields = ['name']


class DivisionAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ConstituencyAdmin(admin.ModelAdmin):
    search_fields = ['name']


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['name']


class SubLocationAdmin(admin.ModelAdmin):
    search_fields = ['name']


class SchoolZoneAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(County, CountyAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Constituency, ConstituencyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SubLocation, SubLocationAdmin)
admin.site.register(SchoolZone, SchoolZoneAdmin)
