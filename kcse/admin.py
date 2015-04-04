from django.contrib import admin

from kcse.models import Result


class ResultAdmin(admin.ModelAdmin):
    search_fields = ['school__name']
    list_filter = ['grade', 'year']

admin.site.register(Result, ResultAdmin)
