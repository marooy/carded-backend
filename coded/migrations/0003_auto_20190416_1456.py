# Generated by Django 2.2 on 2019-04-16 14:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coded', '0002_userinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInfo',
            new_name='Info',
        ),
    ]