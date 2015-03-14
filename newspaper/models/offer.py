from django.db import models
from django.utils.translation import ugettext as _
from .creation import Creation
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Offer(models.Model):
	classifield = models.ForeignKey("newspaper.Classifield", verbose_name=_("classifield"), on_delete=models.CASCADE, )
	author_offer = models.ForeignKey("newspaper.Lector", verbose_name=_("Author"), on_delete=models.CASCADE, )
	date_offer = models.DateTimeField(verbose_name=_("Dating Offer"), null = True, blank=True, )
	value = models.FloatField(default=0, verbose_name=_("Value"),)
	phone = models.IntegerField(max_length=10, verbose_name=_("Phone") , unique=True, validators=[RegexValidator(regex='^\d{10}$', message=_("Length has to be 10"), code=_("Invalid number"))])
    # phone = models.IntegerField(max_length=10)

	def __unicode__(self):
		return self.classifield

	class Meta:
		ordering = ['value']
		verbose_name = _("Offer")
		verbose_name_plural = _("Offers")

	