from django.db import models
from django.utils.translation import ugettext as _

class Page(models.Model):
	title = models.CharField(max_length=20, verbose_name=_("Title"), )
	description = models.CharField(max_length=100, verbose_name=_("Description"), )