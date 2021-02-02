from django.contrib import admin
from .models import Announcement

# Register your models here.

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('announcement', 'is_published', 'date')
    list_display_links = ('announcement',)
    list_editable = ('is_published',)
    search_fields = ('announcement',)
    list_per_page  = 25


admin.site.register(Announcement, AnnouncementAdmin)
