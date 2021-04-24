# Generated by Django 3.1.8 on 2021-04-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0004_auto_20210422_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='isbn',
            name='SN',
            field=models.CharField(default=5001453765, max_length=10, unique=True),
        ),
    ]