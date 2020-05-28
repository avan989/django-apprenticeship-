from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
