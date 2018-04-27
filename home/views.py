	#adapted from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from books.models import Book
from cart.forms import CartAddProductForm

from .forms import SignUpForm

def go_books(request):
    return HttpResponseRedirect("/books/")

def product_list(request):
	books = Book.objects.filter(available=True)[0:3:-1]
	cart_book_form = CartAddProductForm()
	return render(request, 'home/list.html', {'books': books,
												'cart_book_form': cart_book_form})

def terms_and_conditions(request):
	return render(request, 'home/terms.html',{})

def contact_us(request):
	return render(request, 'home/contact.html',{})