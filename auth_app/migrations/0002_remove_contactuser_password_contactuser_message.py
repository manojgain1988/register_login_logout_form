# Generated by Django 5.0.6 on 2024-05-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactuser',
            name='password',
        ),
        migrations.AddField(
            model_name='contactuser',
            name='message',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
