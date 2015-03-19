from .user import User
from django.utils.translation import ugettext as _
from django.contrib.auth.models import Group, Permission
from .lector import Lector

class Anonymous(User):
	def registeringLector(self, form):
		if form.is_valid():
			form.save()
			try:
				u = Lector.objects.get(username = request.POST['username'])
				permission1 = Permission.objects.get(codename='registering_lector')
				permission2 = Permission.objects.get(codename='comment_news')
				permission3 = Permission.objects.get(codename='offer_to_buy')
				u.user_permissions.add(permission1, permission2, permission3)
			except:
				return False
		else:
			return False

	class Meta:
		verbose_name = _("Anonymous")
		verbose_name_plural = _("Anonymous")