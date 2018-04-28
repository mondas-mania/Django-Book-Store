from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from books.models import Book, Genre
from search.forms import SearchBar
from cart.forms import CartAddProductForm

def go_books(request):
    return HttpResponseRedirect("/books/")

def product_list(request):
	books = Book.objects.filter(available=True).order_by('?')[0:3]
	cart_book_form = CartAddProductForm()
	search_form = SearchBar
	genres = Genre.objects.all()
	return render(request, 'home/list.html', {'books': books,
												'genres': genres,
												'cart_book_form': cart_book_form,
												'search_form': search_form})

def terms_and_conditions(request):
	return render(request, 'home/terms.html',{})

def contact_us(request):
	return render(request, 'home/contact.html',{})