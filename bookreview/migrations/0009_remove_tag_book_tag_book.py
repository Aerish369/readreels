# Generated by Django 5.0.6 on 2024-10-07 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0008_alter_tag_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='book',
        ),
        migrations.AddField(
            model_name='tag',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='bookreview.book'),
        ),
    ]
