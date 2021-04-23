import random

from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver

from .models import bookStore,User,Isbn
from django.core.mail import send_mail


@receiver(post_save,sender=bookStore)
def after_book_creation(sender, instance, created, *args, **kwargs):
    def create_new_ref_number():
        return int(random.randint(1000000000, 9999999999))
    if created:
        isbn_instance = Isbn.objects.create(OtherTitle=instance.title,SN=create_new_ref_number())


        isbn_instance.save()
        instance.isbn = isbn_instance

        # send_mail('New Book{}',format(instance.title),'')
    else:
        print("")