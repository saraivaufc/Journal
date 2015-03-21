from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Classifield, Section, Lector
from newspaper.forms import PartialOfferForm
from newspaper.entities import Message, TypeMessage
from django.utils.translation import ugettext as _

def viewClassifield(request, id_classifield):
	try:
		sections = Section.objects.all()
		classifield = Classifield.objects.get(id = id_classifield)
		classifields = Classifield.objects.all().exclude(id = id_classifield)
	except:
		pass
	if request.method == "POST":
		form = PartialOfferForm(request.POST)
		try:
			user = Lector.objects.get(username = request.user.username)
			if user.addOffer(id_classifield, form):
				message = Message(_("Offer was successful!!!"), TypeMessage.SUCCESS)
			else:
				message = Message(_("Your offer must be greater than the minimum value and the best offer currently ranked."), TypeMessage.ERROR)
		except:
			message = Message(_("Failed to make offer!!!"), TypeMessage.ERROR)


	form = PartialOfferForm()
	return render(request, 'newspaper/user/classifield.html', locals())