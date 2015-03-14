from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
from .creation import Creation

class News(models.Model):
	title = models.CharField(max_length=255, verbose_name=_("Title"), )
	subtitle = models.CharField(max_length=500, verbose_name=_("Subtitle"), null=False, blank=False, )
	description = models.TextField(verbose_name=_("Description"), )
	author = models.ForeignKey("newspaper.Journalist", verbose_name=_("Author"), on_delete=models.CASCADE, )
	dating_news = models.DateTimeField(default=datetime.now,verbose_name=_("Dating News"), )
	subsection = models.ForeignKey("newspaper.SubSection", verbose_name=_("SubSection"), on_delete=models.CASCADE, )
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/news/%Y/%m/%d', null=True, blank=True, default=None)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-dating_news']
		verbose_name = _("News")
		verbose_name_plural = _("News")
	
	