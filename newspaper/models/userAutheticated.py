from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser
from .user import User

class UserAutheticated(AbstractUser, User):
	profile_image = models.ImageField(verbose_name=_("Profile Image"),upload_to = 'documents/imagen/profile_image/%Y/%m/%d', null=True, blank=True, default=None)

	def __unicode__(self):
		return self.username

	class Meta:
		db_table = 'auth_user'
		ordering = ['-first_name']
		verbose_name = _("User Autheticated")
		verbose_name_plural = _("Users Autheticated")