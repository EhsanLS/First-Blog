from django.contrib import admin
from .models import Article, Category, Comment


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = ['position', 'title', 'status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {
        'slug': ('title',)
    }


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['category', 'created_at']
    list_display = ['title', 'slug', 'publish', 'status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {
        'slug': ('title',)
    }
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'is_approve']
    list_display = ['__str__', 'author', 'created_at', 'is_approve']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
