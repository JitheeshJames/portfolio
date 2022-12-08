from django.contrib import admin

from .models import Achievements, Catagories, User_Comments, Project

# Register your models here.

admin.site.register(Catagories)
admin.site.register(Achievements)
admin.site.register(User_Comments)
admin.site.register(Project)
