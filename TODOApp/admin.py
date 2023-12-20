from django.contrib import admin
from .models import TodoItem, Tag

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)    

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Tag, TagAdmin)