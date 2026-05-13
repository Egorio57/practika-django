from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'preview_text', 'full_text', 'created_at']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('title', )}