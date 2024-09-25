# Generated by Django 5.0.6 on 2024-09-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0003_profile_email_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='last', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]