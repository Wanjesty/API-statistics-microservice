from django.contrib import admin
from .models import statictics_data

@admin.register(statictics_data)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ("date", "views", "clicks", "cost", "cpc", "cpm")