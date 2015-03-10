from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	profile_image = models.ImageField(verbose_name=_("Profile Image"),upload_to = 'documents/imagen/profile_image/%Y/%m/%d', null=True, blank=True, default=None)
	class Meta:
		db_table = 'auth_user'