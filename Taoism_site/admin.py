from django.contrib import admin
from .models import TK_Category, Blog_Category, TK_Video, Post


admin.site.register(TK_Category)
admin.site.register(TK_Video)
# admin.site.register(Blog_Category)
# admin.site.register(Blog)



@admin.register(Blog_Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'is_published', 'views']
    list_filter = ['category', 'is_published', 'created_at']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'