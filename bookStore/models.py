from django.db import models

# Create your models here.
class bookStore(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title