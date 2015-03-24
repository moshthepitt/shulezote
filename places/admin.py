from django.contrib import admin

from places.models import County, Constituency, Province, District
from places.models import Division, Location, SubLocation, SchoolZone


class CountyAdmin(admin.ModelAdmin):
    pass


class ProvinceAdmin(admin.ModelAdmin):
    pass


class DistrictAdmin(admin.ModelAdmin):
    pass


class DivisionAdmin(admin.ModelAdmin):
    pass


class ConstituencyAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class SubLocationAdmin(admin.ModelAdmin):
    pass


class SchoolZoneAdmin(admin.ModelAdmin):
    pass

admin.site.register(County, CountyAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Constituency, ConstituencyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SubLocation, SubLocationAdmin)
admin.site.register(SchoolZone, SchoolZoneAdmin)
