from django.contrib import admin
from .models import ScanImage


class ImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image_url', 'created_on']


admin.site.register(ScanImage, ImageAdmin)
