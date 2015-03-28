from django.contrib import admin

from staff.models import Staff


class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff, StaffAdmin)
