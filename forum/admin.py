from django.contrib import admin

from forum.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)