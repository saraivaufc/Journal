from django.contrib import admin
from newspaper.models import *

@admin.register(Anonymous)
class AnonymousAdmin(admin.ModelAdmin):
	pass


@admin.register(Classifield)
class ClassifieldAdmin(admin.ModelAdmin):
	pass

@admin.register(Offer)
class OfferdAdmin(admin.ModelAdmin):
	pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	pass

@admin.register(SubSection)
class SubSectionAdmin(admin.ModelAdmin):
	pass

@admin.register(Redator)
class RedatorAdmin(admin.ModelAdmin):
	pass

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
	pass

@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
	pass


@admin.register(UserAutheticated)
class UserAutheticatedAdmin(admin.ModelAdmin):
	pass

