# Generated by Django 5.0.4 on 2024-04-19 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_tareas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='prject',
            new_name='project',
        ),
    ]
