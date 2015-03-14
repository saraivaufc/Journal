from django.db import models
from django.utils.translation import ugettext as _
from .creation import Creation
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Classifield(models.Model):
	title = models.CharField(max_length=50, verbose_name=_("Title"), )
	description = models.TextField(verbose_name=_("Description"), )
	price = models.FloatField(default=0, verbose_name=_("Price"),)
	image = models.ImageField(verbose_name=_("Image"),upload_to = 'documents/imagen/classifield/%Y/%m/%d', null=True, blank=True, default=None)

	creator_classifield = models.ForeignKey("newspaper.Lector", verbose_name=_("Creador Classifield"), null=True, blank=True, on_delete=models.SET_NULL)
	phone = models.IntegerField(max_length=10, verbose_name=_("Phone") , unique=True, validators=[RegexValidator(regex='^\d{10}$', message=_("Length has to be 10"), code=_("Invalid number"))])
    # phone = models.IntegerField(max_length=10)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-title']
		verbose_name = _("Classifield")
		verbose_name_plural = _("Classifields")