	#adapted from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from books.models import Book
from games.models import Game

from .forms import SignUpForm

def go_books(request):
    return HttpResponseRedirect("/books/")

def product_list(request):
	books = Book.objects.filter(available=True)
	games = Game.objects.filter(available=True)
	return render(request, 'home/list.html', {'games': games,
												'books': books})