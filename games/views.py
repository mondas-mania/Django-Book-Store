from django.shortcuts import render, get_object_or_404
from .models import Genre, Game
from cart.forms import CartAddProductForm


def game_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Game.objects.filter(available=True)
    cart_game_form = CartAddProductForm()
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    return render(request, 'games/game/list.html', {'genre': genre,
                                                      'genres': genres,
                                                      'games': games,
                                                      'cart_game_form': cart_game_form})


def game_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_game_form = CartAddProductForm()
    return render(request,
                  'games/game/detail.html',
                   {'book': book,
                    'cart_game_form': cart_game_form})
