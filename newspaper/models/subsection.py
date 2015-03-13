from django.db import models
from django.utils.translation import ugettext as _

class SubSection(models.Model):
	title = models.CharField(max_length=20, verbose_name=_("Title"), )
	description = models.CharField(max_length=100, verbose_name=_("Description"), )
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/page/%Y/%m/%d', null=True, blank=True, default=None)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("SubSection")
		verbose_name_plural = _("SubSections")