#adapted from https://github.com/guinslym/django-by-example-book
from django.contrib import admin
from .models import Game, Developer, Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}
admin.site.register(Genre, GenreAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'developers', 'genre', 'price', 'stock', 'available', 'release_date']
    list_filter = ['available', 'release_date', 'genre']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Game, GameAdmin)

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Developer, DeveloperAdmin)
