from django.contrib import admin

from polls.models import Question, Choice

class ChoiceInline(admin.StackedInline):
# class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display=['question_text','pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']




admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)