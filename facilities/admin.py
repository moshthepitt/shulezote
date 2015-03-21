from django.contrib import admin

from facilities.models import Facility, FacilityRecord

class FacilityAdmin(admin.ModelAdmin):
    pass

class FacilityRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Facility,FacilityAdmin)
admin.site.register(FacilityRecord,FacilityRecordAdmin)
