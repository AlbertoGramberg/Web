# Generated by Django 5.0.4 on 2024-04-29 20:29

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_post_bibliografia_alter_post_contenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='bibliografia',
            field=django_quill.fields.QuillField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=django_quill.fields.QuillField(),
        ),
    ]