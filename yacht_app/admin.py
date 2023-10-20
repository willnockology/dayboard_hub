from django.contrib import admin
from .models import (
    Company, User, Yacht, Category, Form, 
    FormField, Comment, Notification
)

class YachtAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'created_at', 'updated_at')
    list_filter = ('company',)
    search_fields = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'yacht', 'created_at', 'updated_at')
    list_filter = ('yacht',)
    search_fields = ('name', )

class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'yacht', 'status', 'submission_time', 'update_time', 'created_at', 'updated_at')
    list_filter = ('category', 'yacht', 'status')
    search_fields = ('content', )

class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'form', 'yacht', 'created_at', 'updated_at')
    list_filter = ('form', 'yacht',)
    search_fields = ('content', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'form', 'user', 'timestamp', 'created_at', 'updated_at')
    list_filter = ('form', 'user',)
    search_fields = ('content', )

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'status', 'timestamp', 'created_at', 'updated_at')
    list_filter = ('user', 'status',)
    search_fields = ('content', )

# Register your models here.
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Yacht, YachtAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(FormField, FormFieldAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notification, NotificationAdmin)
