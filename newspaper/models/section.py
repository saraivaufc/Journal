from django.db import models
from django.utils.translation import ugettext as _
from .subsection import SubSection


class Section(models.Model):
	title = models.CharField(max_length=50, verbose_name=_("Title"), )
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/sections/%Y/%m/%d/', null=True, blank=True, default=None)
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("Section")
		verbose_name_plural = _("Sections")

	def getSubSections(self):
		try:
			return SubSection.objects.filter(sections = self.id)
		except:
			return []