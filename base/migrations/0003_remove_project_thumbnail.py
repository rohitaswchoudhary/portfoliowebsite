# Generated by Django 3.2.5 on 2021-07-03 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_tags_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='thumbnail',
        ),
    ]