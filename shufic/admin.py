from django.contrib import admin
from shufic.models import Video
from shufic.models import Comment

class VideoInline(admin.StackedInline):
    model = Comment
    extra = 2

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

admin.site.register(Video, VideoAdmin)
# Register your models here.
