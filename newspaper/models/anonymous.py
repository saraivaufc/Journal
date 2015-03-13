from .user import User
from django.utils.translation import ugettext as _

class Anonymous(User):
	def registeringLector(self):
		pass

	class Meta:
		verbose_name = _("Anonymous")
		verbose_name_plural = _("Anonymous")