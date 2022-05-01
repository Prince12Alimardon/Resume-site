from django.contrib import admin
from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = ({'slug': ('title',)})
    filter_horizontal = ('tag',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
