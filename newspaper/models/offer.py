from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class Offer(models.Model):
	author_offer = models.ForeignKey("newspaper.Lector", verbose_name=_("Author"), on_delete=models.CASCADE, )
	date_offer = models.DateTimeField(default=datetime.now, verbose_name=_("Dating Offer"), null = True, blank=True, )
	value = models.FloatField(default=0, verbose_name=_("Value"))
	phone = models.CharField(max_length=15, verbose_name=_("Phone Contact"), null=True, blank=True)
	details = models.TextField(verbose_name=_("Details"), null=True, blank=True)

	def __unicode__(self):
		return str(self.value)

	class Meta:
		ordering = ['-value']
		verbose_name = _("Offer")
		verbose_name_plural = _("Offers")

	