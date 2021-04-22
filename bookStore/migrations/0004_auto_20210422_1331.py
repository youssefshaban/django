# Generated by Django 3.1.8 on 2021-04-22 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0003_auto_20210422_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='isbn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookStore.isbn'),
        ),
        migrations.AlterField(
            model_name='isbn',
            name='SN',
            field=models.CharField(default=6995790508, max_length=10, unique=True),
        ),
    ]