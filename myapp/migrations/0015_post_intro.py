# Generated by Django 5.0.4 on 2024-04-30 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_post_pub_date_alter_post_bibliografia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
