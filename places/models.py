from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

class PlaceModel(models.Model):
    """
    An abstract model for common place fields
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_("Name"), max_length=255, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']

class Province(PlaceModel):
    slug = AutoSlugField(populate_from='name', unique=True)

class County(PlaceModel):
    slug = AutoSlugField(populate_from='name', unique=True)

class District(PlaceModel):
    province = models.ForeignKey(Province, verbose_name=_("Province"))
    slug = AutoSlugField(populate_from='name', unique_with='province__name')

class Division(PlaceModel):
    district = models.ForeignKey(District, verbose_name=_("District"))
    slug = AutoSlugField(populate_from='name', unique_with='district__name')

class Location(PlaceModel):
    division = models.ForeignKey(Division, verbose_name=_("Division"))
    slug = AutoSlugField(populate_from='name', unique_with='division__name')

class SubLocation(PlaceModel):
    location = models.ForeignKey(Location, verbose_name=_("Location"))
    slug = AutoSlugField(populate_from='name', unique_with='location__name')

class Constituency(PlaceModel):
    county = models.ForeignKey(County, verbose_name=_("County"))
    slug = AutoSlugField(populate_from='name', unique_with='county__name')

class SchoolZone(PlaceModel):
    county = models.ForeignKey(County, verbose_name=_("County"))
    slug = AutoSlugField(populate_from='name', unique_with='county__name')
