from django.contrib import admin
from .models import Video

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ["id", "VideoLink", "duration",
                    "thumb",   "embed_code", "tags", "quality"]


admin.site.register(Video, VideoAdmin)

# id = models.CharField(primary_key=True, max_length=30)
# VideoLink = models.TextField(unique=True)
# duration = models.CharField(max_length=200)
# thumb = models.TextField(unique=True)
# embed_code = models.TextField(unique=True)
# tags = ArrayField(models.CharField(max_length=200), blank=True)
# quality = models.CharField(max_length=30)
