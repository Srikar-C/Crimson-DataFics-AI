# Generated by Django 4.2.6 on 2024-01-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsontool', '0004_vidclassifierdisplay'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.URLField()),
                ('video_name', models.CharField(max_length=255)),
                ('downloaded_video_path', models.CharField(max_length=255)),
                ('detection_output', models.TextField()),
            ],
        ),
    ]