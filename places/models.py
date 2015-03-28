from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField


class PlaceModel(models.Model):

    """
    An abstract model for common place fields
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_("Name"), max_length=255, blank=False)

    def meta(self):
        return self._meta

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Province(PlaceModel):
    slug = AutoSlugField(populate_from='name', unique=True)

    def get_absolute_url(self):
        return reverse('place:province', args=[self.slug])

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')


class County(PlaceModel):
    slug = AutoSlugField(populate_from='name', unique=True)

    def get_absolute_url(self):
        return reverse('place:county', args=[self.slug])

    class Meta:
        verbose_name = _('County')
        verbose_name_plural = _('Counties')


class District(PlaceModel):
    province = models.ForeignKey(Province, verbose_name=_("Province"))
    slug = AutoSlugField(populate_from='name', unique_with='province__name')

    def get_absolute_url(self):
        return reverse('place:district', kwargs={'slug': self.slug, 'province_slug': self.province.slug})

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')


class Division(PlaceModel):
    district = models.ForeignKey(District, verbose_name=_("District"))
    slug = AutoSlugField(populate_from='name', unique_with='district__name')

    def get_absolute_url(self):
        return reverse('place:division', kwargs={'slug': self.slug, 'district_slug': self.district.slug})

    class Meta:
        verbose_name = _('Division')
        verbose_name_plural = _('Divisions')


class Location(PlaceModel):
    division = models.ForeignKey(Division, verbose_name=_("Division"))
    slug = AutoSlugField(populate_from='name', unique_with='division__name')

    def get_absolute_url(self):
        return reverse('place:location', kwargs={'slug': self.slug, 'division_slug': self.division.slug})

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class SubLocation(PlaceModel):
    location = models.ForeignKey(Location, verbose_name=_("Location"))
    slug = AutoSlugField(populate_from='name', unique_with='location__name')

    def get_absolute_url(self):
        return reverse('place:sub_location', kwargs={'slug': self.slug, 'location_slug': self.location.slug})

    class Meta:
        verbose_name = _('Sub Location')
        verbose_name_plural = _('Sub Locations')


class Constituency(PlaceModel):
    county = models.ForeignKey(County, verbose_name=_("County"))
    slug = AutoSlugField(populate_from='name', unique_with='county__name')

    def get_absolute_url(self):
        return reverse('place:constituency', kwargs={'slug': self.slug, 'county_slug': self.county.slug})

    class Meta:
        verbose_name = _('Constituency')
        verbose_name_plural = _('Constituencies')


class SchoolZone(PlaceModel):
    county = models.ForeignKey(County, verbose_name=_("County"))
    slug = AutoSlugField(populate_from='name', unique_with='county__name')

    def get_absolute_url(self):
        return reverse('place:school_zone', kwargs={'slug': self.slug, 'county_slug': self.county.slug})

    class Meta:
        verbose_name = _('School Zone')
        verbose_name_plural = _('School Zones')
