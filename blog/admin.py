from django.contrib import admin
from .models import BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class BlogAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'created_on')
    list_display = ('title', 'barber', 'status', 'created_on')
    search_fields = ('title', 'barber', 'content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'created_on', 'name')
    list_display = ('name', 'body', 'approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approved_comment']
    
    def approved_comment(self, request, queryset):
        queryset.update(approved=True)