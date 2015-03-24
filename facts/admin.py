from django.contrib import admin

from facts.models import Fact


class FactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fact, FactAdmin)
