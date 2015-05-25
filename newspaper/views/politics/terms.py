from django.shortcuts import render
from django.utils.translation import ugettext as _

def viewTerms(request):
	return render(request, "newspaper/politics/terms.html", locals())

