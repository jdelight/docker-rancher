from rest_framework import serializers
from films.models import Film


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'url', 'title', 'director')

