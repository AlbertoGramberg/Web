# Generated by Django 5.0.4 on 2024-04-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_comentario_blog_post_delete_blog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('titulo', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
