# Generated by Django 5.0 on 2024-01-13 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leanitem',
            old_name='event_cover_image',
            new_name='cover_image',
        ),
        migrations.RenameField(
            model_name='leanitem',
            old_name='event_discription',
            new_name='discription',
        ),
    ]
