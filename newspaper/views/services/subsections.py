from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _
from newspaper.models import SubSection
import json

def subsections(request):
	titles = []
	for i in SubSection.objects.all():
		titles.append(i.title)
	output = json.dumps({"subsections" : titles})
	return HttpResponse(output)




