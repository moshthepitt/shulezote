from django.contrib.gis import admin
from django.forms import ModelForm

from suit_redactor.widgets import RedactorWidget

from schools.models import School


class SchoolForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'}),
        }


class SchoolAdmin(admin.GeoModelAdmin):
    # form = SchoolForm
    search_fields = ['name']
    list_filter = ['level']

admin.site.register(School, SchoolAdmin)
