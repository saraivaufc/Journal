from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class News(models.Model):
	title = models.CharField(max_length=50, verbose_name=_("Title"), )
	subtitle = models.CharField(max_length=150, verbose_name=_("Subtitle"), null=False, blank=False, )
	text = models.TextField(verbose_name=_("Text"), )
	author = models.ForeignKey("newspaper.User", verbose_name=_("Author"), on_delete=models.CASCADE, )
	dating_news = models.DateTimeField(default=datetime.now,verbose_name=_("Dating News"), )
	page = models.ForeignKey("newspaper.Page", verbose_name=_("Page"), on_delete=models.CASCADE, )
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/news/%Y/%m/%d', null=True, blank=True, default=None)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("News")
		verbose_name_plural = _("News")
	
    