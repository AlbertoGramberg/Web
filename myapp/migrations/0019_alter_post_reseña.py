# Generated by Django 5.0.4 on 2024-04-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_post_reseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reseña',
            field=models.TextField(max_length=400),
        ),
    ]
