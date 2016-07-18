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

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.user.userprofile.is_member("pyuka"):
            self.readonly_fields = [
                'name',
                'code',
                'slug',
                'address',
                'level',
                'school_type',
                'student_gender',
                'ownership',
                'sponsor',
                'student_needs',
                'is_active',
                'county',
                'constituency',
                'province',
                'district',
                'division',
                'location',
                'sub_location',
                'school_zone',
                'coordinates',
            ]

        return super(SchoolAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

admin.site.register(School, SchoolAdmin)
