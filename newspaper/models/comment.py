from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class Comment(models.Model):
	author = models.ForeignKey("newspaper.Lector", verbose_name=_("Author"), on_delete=models.CASCADE, )
	text = models.TextField(verbose_name=_("Text"),)
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/comment/%Y/%m/%d', null=True, blank=True, default=None)
	dating_comment = models.DateTimeField(default=datetime.now,verbose_name=_("Dating Comment"), blank=True )
	
	def __unicode__(self):
		return str(self.author)

	class Meta:
		ordering = ['-dating_comment']
		verbose_name = _("Comment")
		verbose_name_plural = _("Comments")

	def getAuthor(self):
		from .lector import Lector
		try:
			return Lector.objects.get(id = self.author_id)
		except:
			return None
