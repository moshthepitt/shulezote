from django.db import models
from django.utils.translation import ugettext_lazy as _

from schools.models import School


class Facility(models.Model):

    """
    Meant to store individual types of facilities that we are tracking
    e.g. Toilets, Classrooms, etc
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_("Name of facility"), max_length=255, blank=False)

    def __unicode__(self):
        return self.name


class FacilityRecord(models.Model):

    """
    Track a facility's record for a given school as at a given time
    The period essentially only tracks the year, for example the initial data comes from 2007
    It is recommended to put the last date of the year e.g. 12-12-2007
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    facility = models.ForeignKey(Facility, verbose_name=_("Facility"))
    school = models.ForeignKey(School, verbose_name=_("School"))
    period = models.DateField(_("Period"))
    boys = models.PositiveIntegerField(_("Boys"), default=0)
    girls = models.PositiveIntegerField(_("Girls"), default=0)
    total = models.PositiveIntegerField(_("Total"), default=0)

    def __unicode__(self):
        return "%s %s %s" % (self.school, self.facility, self.period)
