# Generated by Django 5.0.6 on 2024-10-06 11:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0006_remove_profile_email_remove_profile_first_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('book', 'reviewer')},
        ),
    ]