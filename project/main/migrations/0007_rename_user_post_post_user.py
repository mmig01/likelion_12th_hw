# Generated by Django 5.0.3 on 2024-05-06 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='post_user',
        ),
    ]
