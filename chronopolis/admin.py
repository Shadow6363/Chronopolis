from django.contrib import admin
from chronopolis.models import Survey, Question

class QuestionInline(admin.TabularInline):
	model = Question
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('survey', 'text', 'type')

class SurveyAdmin(admin.ModelAdmin):
	fields = ['title', 'instructions']
	inlines = [QuestionInline]
	list_display = ('title', 'instructions', 'user')

	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
		obj.save()

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
