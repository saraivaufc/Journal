from django.db import models
from django.utils.translation import ugettext as _
from .userAuthenticated import UserAuthenticated

class Journalist(UserAuthenticated):
	def registeringNews(self, form): 
		form.setAuthor(self.id)
		if form.is_valid():
			form.updateNameImage()
			form.save()
			return True
		else:
			return False
	
	def deleteNews(self, id_news):
		try:
			from newspaper.models import News
			News.objects.get(id = id_news).delete()
			return True
		except:
			return False

	def editNews(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = _("Journalist")
		verbose_name_plural = _("Journalists")

		permissions = (("keep_news", "Keep News"),
                      )