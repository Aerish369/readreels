# Generated by Django 5.0.6 on 2024-10-07 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0009_remove_tag_book_tag_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='bookreview.tag'),
        ),
    ]
