# Generated by Django 4.2.3 on 2023-12-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_haven_app', '0013_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sections',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
