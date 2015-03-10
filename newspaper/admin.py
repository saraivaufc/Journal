from django.contrib import admin
from newspaper.models import *

@admin.register(Classifield)
class ClassifieldAdmin(admin.ModelAdmin):
	pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	pass

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass
