from django.contrib import admin
from films.models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


