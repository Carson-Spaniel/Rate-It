# Generated by Django 4.2.3 on 2023-12-22 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends_haven_app', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fans',
            field=models.CharField(default=0, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='idols',
            field=models.CharField(default=0, max_length=50000, null=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, null=True, upload_to='')),
                ('rate', models.IntegerField(default=0)),
                ('caption', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ingredients', models.CharField(default=None, max_length=5000, null=True)),
                ('instructions', models.CharField(default=None, max_length=5000, null=True)),
                ('author', models.CharField(default=None, max_length=100, null=True)),
                ('TV_where_to_watch', models.CharField(default=None, max_length=5000, null=True)),
                ('Movie_where_to_watch', models.CharField(default=None, max_length=5000, null=True)),
                ('community_rate', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friends_haven_app.profile')),
            ],
        ),
    ]
