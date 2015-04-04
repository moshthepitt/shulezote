from django.db import models
from django.utils.translation import ugettext_lazy as _

from schools.models import School


class Result(models.Model):
    """
    This model stores examination results for
    KCSE (Kenya Certificate of Secondary Education) exams
    """
    # schoo level
    MALE = '1'
    FEMALE = '2'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    year = models.IntegerField(_("Year"))
    district_code = models.CharField(_("District Code"), max_length=255, blank=True)
    school_code = models.CharField(_("School Code"), max_length=255, blank=True)
    knec_code = models.CharField(_("KNEC Code"), max_length=255, blank=True)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDER_CHOICES, blank=False, help_text=_(
        "Gender"))
    school = models.ForeignKey(School, verbose_name=_("School"))
    grade = models.CharField(_("Grade"), max_length=2)
    mean_grade = models.DecimalField(_("Mean Grade"), max_digits=5, decimal_places=2)
    frequency = models.IntegerField(_("Frequency"))

    class Meta:
        verbose_name = _("KCSE Result")
        verbose_name_plural = _("KCSE Results")

    def __str__(self):
        return "%s %s %s" % (self.school.name, self.grade, self.year)
