# Generated by Django 5.0.6 on 2025-01-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0016_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, default='bookreview/images/default.jpg', upload_to='bookreview/images'),
        ),
    ]