from django.db import models
from multiselectfield import MultiSelectField


class Actor(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='actors/photos/')

    def __str__(self):
        return self.full_name


class Show(models.Model):
    title = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    actors = models.ManyToManyField(Actor)

    type_choices = (('film', 'Film'),
                    ('tv', 'TV Show'))
    type = models.CharField(max_length=255, choices=type_choices)
    preview = models.ImageField(upload_to='shows/previews/')
    video = models.FileField(upload_to='shows/films/')

    description = models.TextField()

    genre_choices = (('action', 'action'),
                     ('comedy', 'comedy'),
                     ('drama', 'drama'),
                     ('fantasy', 'fantasy'),
                     ('horror', 'horror'),
                     ('mystery', 'mystery'),
                     ('romance', 'romance'),
                     ('thriller', 'thriller'),
                     ('western', 'western'))
    genre = MultiSelectField(choices=genre_choices)

    def __str__(self):
        return f"{self.type.upper()}: «{self.title}»"

    class Meta:
        verbose_name = "Шоу"
        verbose_name_plural = "Шоу"
