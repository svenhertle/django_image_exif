from django.contrib import admin

from filer.admin.imageadmin import ImageAdmin

from .models import ExifData

class ExifDataInline(admin.TabularInline):
    model = ExifData

ImageAdmin.inlines = ImageAdmin.inlines[:] + [ExifDataInline]
