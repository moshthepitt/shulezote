from django.db import models
from django.utils.translation import ugettext_lazy as _

from schools.models import School

class Staff(models.Model):
    """
    stores some information about teahcers at a school as of a certain period
    The period essentially only tracks the year, for example the initial data comes from 2007
    It is recommended to put the last date of the year e.g. 12-12-2007
    """
    TSC_MALE = "A"
    TSC_FEMALE = "B"
    LOCAL_MALE = "C"
    LOCAL_FEMALE = "D"
    PTA_MALE = "E"
    PTA_FEMALE = "F"
    OTHER_MALE = "G"
    OTHER_FEMALE = "H"
    NON_TEACHING_MALE = "I"
    NON_TEACHING_FEMALE = "J"
    TYPE_CHOICES = (
        (TSC_MALE, _("TSC Male Teachers")),
        (TSC_FEMALE, _("TSC Female Teachers")),
        (LOCAL_MALE, _("Local Authority Male Teachers")),
        (LOCAL_FEMALE, _("Local Authority Female Teachers")),
        (PTA_MALE, _("PTA Board of Governors Male Teacher")),
        (PTA_FEMALE, _("PTA Board of Governors Female Teacher")),
        (OTHER_MALE, _("Other Male Teachers")),
        (OTHER_FEMALE, _("Other Female Teachers")),
        (NON_TEACHING_MALE, _("Non Teaching Staff Male")),
        (NON_TEACHING_FEMALE, _("Non Teaching Staff Female"))
    )

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    school = models.ForeignKey(School, verbose_name=_("School"))
    period = models.DateField(_("Period"))
    staff_type = models.CharField(_("Type of staff"), max_length=1, choices=TYPE_CHOICES, blank=False)
    number = models.PositiveIntegerField(_("Number"), default=0)
    is_teacher = models.BooleanField(_('Teacher'), default=True,
            help_text=_('Designates whether this staff member is a teacher'))

    def __unicode__(self):
        return "%s %s %s" %(self.get_staff_type_display(), self.school, self.period)
