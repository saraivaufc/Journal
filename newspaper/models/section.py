from django.db import models
from django.utils.translation import ugettext as _

class Section(models.Model):
	title = models.CharField(max_length=20, verbose_name=_("Title"), )
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/page/%Y/%m/%d', null=True, blank=True, default=None)
	subsections = models.ManyToManyField("newspaper.SubSection", verbose_name=_("SubSections"), null=True, blank=True)
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("Section")
		verbose_name_plural = _("Sections")