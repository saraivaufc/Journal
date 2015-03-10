from django.db import models
from django.utils.translation import ugettext as _

class Role(models.Model):
	role = models.CharField(max_length=20, verbose_name=_("Role"), )