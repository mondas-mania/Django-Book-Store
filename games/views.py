from django.shortcuts import render, get_object_or_404
from .models import Genre, Game
from books.models import Book
from cart.forms import CartAddProductForm


def game_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    games = Game.objects.filter(available=True)
    books = Book.objects.filter(available=True)
    cart_game_form = CartAddProductForm()
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        games = games.filter(genre=genre)
    return render(request, 'games/game/list.html', {'genre': genre,
                                                      'genres': genres,
                                                      'games': games,
                                                      'books': books,
                                                      'cart_game_form': cart_game_form})


def game_detail(request, id, slug):
    game = get_object_or_404(Game, id=id, slug=slug, available=True)
    cart_game_form = CartAddProductForm()
    return render(request,
                  'games/game/detail.html',
                   {'game': game,
                    'cart_game_form': cart_game_form})
