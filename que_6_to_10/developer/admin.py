from django.contrib import admin
from developer.models import developers

@admin.register(developers)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialist', 'experience', 'contact')
    search_fields = ('name', 'specialist')
    list_filter = ('specialist',)

