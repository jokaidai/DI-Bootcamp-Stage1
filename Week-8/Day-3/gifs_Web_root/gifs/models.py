from django.db import models

# Create your models here.

class Gif(models.Model):

    title = models.CharField(max_length = 50)
    url = models.URLField(max_length = 100)
    uploader_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):

    name = models.CharField(max_length = 50, unique = True)
    gif = models.ManyToManyField(Gif, related_name = 'categories')

    def __str__(self) -> str:
        return self.name
