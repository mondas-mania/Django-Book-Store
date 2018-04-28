from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from books.models import Book
from cart.forms import CartAddProductForm
from django.db.models import Q


def search_book(request):
		phrase = request.POST.get("phrase", "")
		phrase = phrase.strip()
		books = Book.objects.filter(Q(title__icontains=phrase) | Q(description__icontains=phrase) 
									| Q(authors__first_name__icontains=phrase) | Q(genre__genre__icontains=phrase)
									| Q(authors__last_name__icontains=phrase))
		cart_book_form = CartAddProductForm()
		return render(request, 'search/detail.html', {'books': books,
																'phrase': phrase,
																'cart_book_form': cart_book_form})
