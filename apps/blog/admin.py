import datetime
from django.urls import reverse
from django.contrib import admin

from .models import Post, Categories, CategoryPostDesa, PostDesa
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_added']

admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
admin.site.register(CategoryPostDesa)
admin.site.register(PostDesa, PostAdmin)
