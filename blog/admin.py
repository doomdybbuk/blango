# from django.contrib import admin
# from blog.models import Tag, Post

# # Register your models here.
# admin.site.register(Tag)
# class PostAdmin(admin.ModelAdmin):
#   prepopulated_fields = {"slug":("title",)}
#   list_display = ('slug','published_at')
# admin.site.register(Post,PostAdmin)
# admin.site.register(Tag)
# admin.site.register(Comment)

from django.contrib import admin
from blog.models import Tag , Post , Comment

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("title",)}

admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)