from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import Classifield, Section, Lector
from newspaper.forms import PartialOfferForm
from newspaper.entities import Message, TypeMessage,TextMessage
from django.utils.translation import ugettext as _
from newspaper.utils import filterList
from .home import home
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

#@cache_page(60 * 15)
@csrf_protect
def viewClassifield(request, id_classifield):
	message = None
	try:
		sections = Section.objects.all()
		try:
			classifield = Classifield.objects.get(id = id_classifield)
		except:
			message = Message(TextMessage.CLASSIFIELD_NOT_FOUND, TypeMessage.ERROR)
			return home(request, None, None, message)

		classifields = Classifield.objects.all().exclude(id = id_classifield)
	except:
		pass
	if request.method == "POST":
		form = PartialOfferForm(request.POST)
		try:
			try:
				user = Lector.objects.get(username = request.user.username)
			except:
				message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.SUCCESS)
				return manager(request, None, None, message)

			if user.addOffer(id_classifield, form):
				message = Message(TextMessage.OFFER_SUCCESS_ADD, TypeMessage.SUCCESS)
			else:
				message = Message(TextMessage.OFFER_REQUIRED_MINIMUM_VALUE, TypeMessage.ERROR)
		except:
			message = Message(TextMessage.OFFER_ERROR_ADD, TypeMessage.ERROR)

	form = PartialOfferForm()
	classifields = filterList(classifields, 1, 3)
	contex = {'form' : form, 
			  'message' : message, 
			  'sections': sections,
			  'classifield': classifield,
			  'classifields': classifields,}
	return render(request, 'newspaper/user/classifield.html', contex)