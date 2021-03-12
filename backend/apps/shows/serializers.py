from rest_framework import serializers

from . import models


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ['full_name', 'photo']


class ShowSerializer(serializers.ModelSerializer):
    genre = serializers.MultipleChoiceField(choices=models.Show.genre_choices)
    actors = ActorSerializer(many=True)

    class Meta:
        model = models.Show
        fields = ['id', 'title', 'rating', 'actors', 'preview', 'genre', 'type']
