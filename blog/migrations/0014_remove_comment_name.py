# Generated by Django 3.1.8 on 2021-11-26 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20211126_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
