# from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from places.models import County, Constituency, Province, District
from places.models import Division, Location, SubLocation, SchoolZone


class School(models.Model):

    """
    This model stores information about schools
    """
    # N/A
    NOT_KNOWN = "Z"
    # schoo level
    PRIMARY = '1'
    SECONDARY = '2'
    LEVEL_CHOICES = (
        (PRIMARY, _('Primary School')),
        (SECONDARY, _('Secondary School'))
    )
    # school owner
    PUBLIC = '1'
    PRIVATE = '2'
    OWNERSHIP_CHOICES = (
        (PUBLIC, _('Public')),
        (PRIVATE, _('Private'))
    )
    # student gender
    BOYS = '1'
    GIRLS = '2'
    MIXED = '3'
    GENDER_CHOICES = (
        (BOYS, _('Boys')),
        (GIRLS, _('Girls')),
        (MIXED, _('Mixed')),
        (NOT_KNOWN, _("N/A")),
    )
    # day or boarding
    DAY = '1'
    BOARDING = '2'
    DAY_AND_BOARDING = '3'
    TYPE_CHOICES = (
        (DAY, _('Day')),
        (BOARDING, _('Boarding')),
        (DAY_AND_BOARDING, _('Day & Boarding')),
        (NOT_KNOWN, _("N/A")),
    )
    # student needs
    ORDINARY = '1'
    SPECIAL = '2'
    INTEGRATED = '3'
    STUDENT_NEED_CHOICES = (
        (ORDINARY, _('Ordinary')),
        (SPECIAL, _('Special')),
        (INTEGRATED, _('Integrated')),
    )
    # sponsor choices
    GOVERNMENT = '1'
    RELIGIOUS = '2'
    COMMUNITY = '3'
    NGO = "4"
    PRIVATE_INDIVIDUAL = "5"
    SPONSOR_CHOICES = (
        (GOVERNMENT, _('Central Government/DEB')),
        (RELIGIOUS, _('Religious Organisation')),
        (COMMUNITY, _('Community')),
        (NGO, _('NGO/CBO')),
        (PRIVATE_INDIVIDUAL, _('Private Individual')),
        (NOT_KNOWN, _("N/A")),
    )

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    code = models.CharField(_("Code"), max_length=255, blank=True)
    name = models.CharField(_("Name of School"), max_length=255, blank=False)
    slug = AutoSlugField(populate_from='name', unique=True)
    address = models.CharField(_("Address"), max_length=255, blank=True)
    level = models.CharField(_("Level"), max_length=1, choices=LEVEL_CHOICES, blank=False, help_text=_(
        "Primary or secondary school"))
    school_type = models.CharField(
        _("School Type"), max_length=1, choices=TYPE_CHOICES, default=NOT_KNOWN, help_text=_("Day, Boarding or Both?"))
    student_gender = models.CharField(_("Student Gender"), max_length=1, choices=GENDER_CHOICES, default=NOT_KNOWN, help_text=_(
        "Boys school, Girls school, or mixed"))
    ownership = models.CharField(
        _("Ownership"), max_length=1, choices=OWNERSHIP_CHOICES, default=PUBLIC, help_text=_("Private or public"))
    sponsor = models.CharField(
        _("School Sponsor"), max_length=1, choices=SPONSOR_CHOICES, default=NOT_KNOWN)
    student_needs = models.CharField(
        _("Student Needs"), max_length=1, choices=STUDENT_NEED_CHOICES, default=ORDINARY, help_text=_("Ordinary, Special or Integrated"))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this school is active.'))

    county = models.ForeignKey(County, verbose_name=_("County"))
    constituency = models.ForeignKey(
        Constituency, verbose_name=_("Constituency"))
    province = models.ForeignKey(
        Province, verbose_name=_("Province"), blank=True, null=True, default=None)
    district = models.ForeignKey(
        District, verbose_name=_("District"), blank=True, null=True, default=None)
    division = models.ForeignKey(
        Division, verbose_name=_("Division"), blank=True, null=True, default=None)
    location = models.ForeignKey(
        Location, verbose_name=_("Location"), blank=True, null=True, default=None)
    sub_location = models.ForeignKey(SubLocation, verbose_name=_(
        "Sub Location"), blank=True, null=True, default=None)
    school_zone = models.ForeignKey(
        SchoolZone, verbose_name=_("School Zone"), blank=True, null=True, default=None)

    # Geo Django field to store a point
    coordinates = models.PointField(_("Coordinates"), null=False, blank=False, help_text=_(
        "Represented as (longitude, latitude)"))

    # You MUST use GeoManager to make Geo Queries
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
