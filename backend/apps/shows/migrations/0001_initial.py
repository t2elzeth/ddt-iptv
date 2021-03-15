# Generated by Django 3.1.7 on 2021-03-15 03:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='actors/photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('film', 'Film'), ('tv', 'TV Show')], max_length=255)),
                ('preview', models.ImageField(upload_to='shows/previews/')),
                ('video', models.FileField(upload_to='shows/films/')),
                ('description', models.TextField()),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama'), ('fantasy', 'fantasy'), ('horror', 'horror'), ('mystery', 'mystery'), ('romance', 'romance'), ('thriller', 'thriller'), ('western', 'western')], max_length=67)),
                ('actors', models.ManyToManyField(to='shows.Actor')),
            ],
            options={
                'verbose_name': 'Шоу',
                'verbose_name_plural': 'Шоу',
            },
        ),
    ]
