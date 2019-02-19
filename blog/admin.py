from django.contrib import admin

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'writer')

from .models import Quote

admin.site.register(Quote, QuoteAdmin)
