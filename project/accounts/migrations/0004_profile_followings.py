# Generated by Django 5.0.3 on 2024-06-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_mbit_profile_mbti'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to='accounts.profile'),
        ),
    ]
