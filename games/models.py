#adapted from https://github.com/guinslym/django-by-example-book
from django.db import models
from django.core.urlresolvers import reverse

class Developer(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=30, db_index = True)

    def __str__(self):
        return '%s' % (self.name)

class Genre(models.Model):
    genre = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, db_index = True, unique = True)

    class Meta:
        ordering = ('genre',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
		return self.genre

    def get_absolute_url(self):
        return reverse('games:game_list_by_genre', args=[self.slug])

    def get_capitalised_name(self):
        return self.genre.capitalize()

class Game(models.Model):
    genre = models.ForeignKey(Genre, related_name='games')
    title = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    developers = models.ForeignKey(Developer)
#   image = models.ImageField(upload_to='games/%Y/%m/%d', blank=True)
    image = models.ImageField(upload_to='games/games_img', blank=True)
    description = models.TextField(blank = True, null = True)
    release_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-release_date',)
        index_together = (('id', 'slug'),)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
        return reverse('games:game_detail', args=[self.id, self.slug])