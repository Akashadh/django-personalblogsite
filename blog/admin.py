from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.site_header = "AkashSite"


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("created_on", "status")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
