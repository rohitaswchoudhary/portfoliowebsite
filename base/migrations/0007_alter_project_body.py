# Generated by Django 3.2.5 on 2021-07-04 19:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_project_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
