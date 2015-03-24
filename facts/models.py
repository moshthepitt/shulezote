from django.db import models
from django.utils.translation import ugettext_lazy as _

from schools.models import School
from facilities.models import Facility
from staff.models import Staff


class Fact(models.Model):

    """
    Stores facts about a school as at a certain period
    The period essentially only tracks the year, for example the initial data comes from 2007
    It is recommended to put the last date of the year e.g. 12-12-2007

    The fact can optionally be tied to a Staff Object or a Facility Object
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_("Fact"), max_length=255, blank=False)
    value = models.CharField(_("Fact Value"), max_length=255, blank=False)
    period = models.DateField(_("Period"))
    school = models.ForeignKey(School, verbose_name=_("School"))
    facility = models.ForeignKey(
        Facility, verbose_name=_("Facility"), blank=True, null=True, default=None)
    staff = models.ForeignKey(Staff, verbose_name=_("Staff"), blank=True, null=True, default=None)

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.school, self.period)
