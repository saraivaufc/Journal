from django.db import models
from django.utils.translation import ugettext as _
from .creation import Creation
from datetime import datetime

class Offer(models.Model):
	author_offer = models.ForeignKey("newspaper.Lector", verbose_name=_("Author"), on_delete=models.CASCADE, )
	date_offer = models.DateTimeField(verbose_name=_("Dating Offer"), null = True, blank=True, )
	value = models.FloatField(default=0, verbose_name=_("Value"),)
	phone = models.IntegerField(max_length=12, verbose_name=_("Phone"),)
    # phone = models.IntegerField(max_length=10)


	class Meta:
		ordering = ['value']
		verbose_name = _("Offer")
		verbose_name_plural = _("Offers")

	