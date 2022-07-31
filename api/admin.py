from atexit import register
from django.contrib import admin
from . import models as BlogModel

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogModel.Blog)
admin.site.register(BlogModel.Comments)