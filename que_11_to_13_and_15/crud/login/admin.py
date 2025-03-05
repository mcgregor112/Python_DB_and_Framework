from django.contrib import admin

# Register your models here.
from django.contrib import admin
from login.models import crud

class crudadmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('email',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'password'),
        }),
    )

admin.site.register(crud ,crudadmin)

