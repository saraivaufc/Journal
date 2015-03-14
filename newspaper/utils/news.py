from newspaper.models import News, Section, SubSection

def getSections(news):
	sections = []
	subsection = SubSection.objects.get(id = news.subsection_id)
	for i in subsection.sections.all():
		sections.append(i)
	return sections

def getNewsFromSection(section):
	subsections_all = SubSection.objects.all()
	subsections = []
	for i in subsections_all:
		belongs_section = False
		for k in i.sections.all():
			if section.id == k.id:
				belongs_section = True
		if belongs_section:
			subsections.append(i)
	news_all = News.objects.all()
	news = []
	for i in news_all:
		belongs_subsection = False
		for k in subsections:
			if i.subsection_id == k.id:
				belongs_subsection = True
		if belongs_subsection:
			news.append(i)
	return news






