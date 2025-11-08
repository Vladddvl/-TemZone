from django.contrib import admin
from .models import Category, Topic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'view_count']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'short_description']
    readonly_fields = ['created_at']