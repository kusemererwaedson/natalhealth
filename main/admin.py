from django.contrib import admin

# Register your models here.
from .models import BabyWeek, PregnancyDetails, InsightCategory, Insight

@admin.register(BabyWeek)
class BabyWeekAdmin(admin.ModelAdmin):
    list_display = ('week_number', 'average_weight', 'average_size')
    ordering = ('week_number',)

# Register PregnancyDetails model
@admin.register(PregnancyDetails)
class PregnancyDetailsAdmin(admin.ModelAdmin):
    list_display = ('nin','name','baby_sex', 'due_date_choice', 'first_child', 'age_group', 'due_date')
    list_filter = ('nin','name','baby_sex', 'due_date_choice', 'first_child', 'age_group')
    search_fields = ('nin','name','baby_sex', 'first_child', 'age_group')
    ordering = ('due_date',)

@admin.register(InsightCategory)
class InsightCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','image')
    list_filter = ('category',)
    search_fields = ('title', 'body')