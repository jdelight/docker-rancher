from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{0}'.format(self.title)

