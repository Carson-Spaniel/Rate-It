# Generated by Django 4.2.3 on 2023-12-22 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_haven_app', '0002_alter_profile_fans_alter_profile_idols_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
