from django.contrib import admin
from .models import Post, Category, Tag, Contact

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'user']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
