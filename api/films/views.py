from films.models import Film
from films.serializers import FilmSerializer
from rest_framework import generics


class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
