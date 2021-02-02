from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'join_date',)
    list_display_links = ('id','name')
    search_fields = ('name', )
    list_per_page = 25


admin.site.register(Member, MemberAdmin)
