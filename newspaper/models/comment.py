from django.db import models
from django.utils.translation import ugettext as _
from .creation import Creation
from datetime import datetime

class Comment(models.Model):
	news = models.ForeignKey("newspaper.News", verbose_name=_("News"), on_delete=models.CASCADE, )
	author = models.ForeignKey("newspaper.Lector", verbose_name=_("Author"), on_delete=models.CASCADE, )
	text = models.TextField(verbose_name=_("Text"),)
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/comment/%Y/%m/%d', null=True, blank=True, default=None)
	dating_comment = models.DateTimeField(default=datetime.now,verbose_name=_("Dating Comment"), )
	
	def __unicode__(self):
		return self.news

	class Meta:
		ordering = ['-dating_comment']
		verbose_name = _("Comment")
		verbose_name_plural = _("Comments")