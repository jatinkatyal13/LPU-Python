from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    video_file = models.FileField()

    tags = models.ManyToManyField("main.Tag")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
