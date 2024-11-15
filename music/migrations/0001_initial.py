# Generated by Django 5.1.2 on 2024-11-03 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=53, verbose_name='Artist Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Artist Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last artist update')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=50, verbose_name='Album Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Album Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last album update')),
                ('thumbnail', models.ImageField(default=True, upload_to='img/', verbose_name='Thumbnail')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist', verbose_name='Artist Album')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='img/', verbose_name='Thumbnail')),
                ('song_title', models.CharField(max_length=255, verbose_name='Song Title')),
                ('song', models.FileField(help_text='Any audio format supported', upload_to='songs/', verbose_name='Song')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Song Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Song update')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album', verbose_name='MusicModel Album')),
            ],
            options={
                'verbose_name': 'Music',
                'verbose_name_plural': 'Musics',
            },
        ),
    ]
