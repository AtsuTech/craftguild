# Generated by Django 5.0 on 2024-01-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionitem',
            name='inquiry',
            field=models.CharField(max_length=255, verbose_name='質問)'),
        ),
    ]
