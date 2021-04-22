from django.db import models
from django.contrib.auth.models import User
import random

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

def create_new_ref_number():
    return int(random.randint(1000000000, 9999999999))


class Isbn(models.Model):
    OtherTitle= models.CharField(max_length=255)
    SN= models.CharField(max_length=10, unique=True, default=create_new_ref_number())

    def __str__(self):
        return f"{self.OtherTitle} Title | {self.SN} serial Number"




class bookStore(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="books")
    isbn = models.ForeignKey(Isbn, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True)



    def __str__(self):
        return self.title