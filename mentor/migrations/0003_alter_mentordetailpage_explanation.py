# Generated by Django 5.0 on 2024-01-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_alter_mentorintroductionpage_page_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentordetailpage',
            name='explanation',
            field=models.TextField(blank=True, null=True, verbose_name='メンターの紹介文'),
        ),
    ]
