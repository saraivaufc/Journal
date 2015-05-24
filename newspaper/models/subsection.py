from django.db import models
from django.utils.translation import ugettext as _

class SubSection(models.Model):
	title = models.CharField(max_length=50, verbose_name=_("Title"), )
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/subsections/%Y/%m/%d/', null=True, blank=True, default=None)
	sections = models.ManyToManyField("newspaper.Section", verbose_name=_("Sections"))
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("SubSection")
		verbose_name_plural = _("SubSections")