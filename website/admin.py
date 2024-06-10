from django.contrib import admin
from website.models import content
# Register your models here.

class contentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty_value'
    list_display = ['name', 'subject', 'email','created_date']
    list_filter = ['email']
    search_fields = ['email', 'name', 'subject', 'massage']
    

admin.site.register(content,contentadmin)