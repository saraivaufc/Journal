from django.db import models
from django.utils.translation import ugettext as _
from .userAuthenticated import UserAuthenticated
from newspaper.models import Journalist, Section, SubSection, Classifield
from django.contrib.auth.models import Group, Permission

class Redator(UserAuthenticated):
	def registeringJournalist(self, form):
		if form.is_valid():	
			form.save()
			data = form.cleaned_data
			username = data['username']
			u = Journalist.objects.get(username = username)
			permission1 = Permission.objects.get(codename='keep_news')
			permission2 = Permission.objects.get(codename='access_manager')
			u.user_permissions.add(permission1, permission2,)
			return True
		else:
			return False
	def registeringRedator(self, form):
		if form.is_valid():	
			form.save()
			data = form.cleaned_data
			username = data['username']
			from newspaper.models import Redator
			u = Redator.objects.get(username = username)
			permission1 = Permission.objects.get(codename='keep_journalist')
			permission2 = Permission.objects.get(codename='keep_redator')
			permission3 = Permission.objects.get(codename='keep_classifield')
			permission4 = Permission.objects.get(codename='keep_section')
			permission5 = Permission.objects.get(codename='keep_subsection')
			permission6 = Permission.objects.filter(codename='delete_news')[0]
			permission7 = Permission.objects.get(codename='access_manager')
			u.user_permissions.add(permission1, permission2,permission3,permission4,permission5,permission6,permission7)
			return True
		else:
			return False

	def editJournalist(self,form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def editRedator(self,form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def remJournalist(self, id):
		try:
			Journalist.objects.get(id = id).delete()
			return True
		except:
			return False

	def remRedator(self, id):
		try:
			from newspaper.models import Redator
			Redator.objects.get(id = id).delete()
			return True
		except:
			return False


	def deleteNews(self, id_news):
		try:
			from newspaper.models import News
			News.objects.get(id = id_news).delete()
			return True
		except:
			return False


	def registeringSection(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False
	def editSection(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def remSection(self, id_section):
		try:
			Section.objects.get(id = id_section).delete()
			return True
		except:
			return False



	def registeringSubSection(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def editSubSection(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def remSubSection(self, id_subsection):
		try:
			SubSection.objects.get(id = id_subsection).delete()
			return True
		except:
			return False


	def registeringClassifield(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def remClassifield(self, id_classifield):
		try:
			Classifield.objects.get(id = id_classifield).delete()
			return True
		except:
			return False

	def editClassifield(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = _("Redator")
		verbose_name_plural = _("Redators")
		permissions = (("keep_journalist", "Keep Journalist"),
					   ("keep_redator", "Keep Redator"),
                       ("keep_classifield", "Keep Classifield"),
                       ("keep_section", "Keep Section"),
                       ("keep_subsection", "Keep SubSection"),
                       ("delete_news", "Delete News"),
                      )