from django.db import models
from django.utils.translation import ugettext as _

class Classifield(models.Model):
	title = models.CharField(max_length=50, verbose_name=_("Title"), )
	text = models.TextField(verbose_name=_("Text"), )
	price = models.FloatField(default=0, verbose_name=_("Price"),)
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/classifield/%Y/%m/%d', null=True, blank=True, default=None)

	best_offer = models.FloatField(verbose_name=_("Best Offer"), )
	date_offer = models.DateTimeField(verbose_name=_("Dating Offer"), null = True, blank=True, )
	author_offer = models.ForeignKey("newspaper.Lector", verbose_name=_("Author Offer"), null=True, blank=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("Classifield")
		verbose_name_plural = _("Classifields")