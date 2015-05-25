from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import Section
import json

def sections(request):
	titles = []
	for i in Section.objects.all():
		titles.append(i.title)
	output = json.dumps({"sections" : titles})
	return HttpResponse(output)
