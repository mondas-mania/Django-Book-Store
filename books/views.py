from django.shortcuts import render, get_object_or_404
from .models import Genre, Book
from search.forms import SearchBar, SortChoices
from cart.forms import CartAddProductForm

sort_dict = {
  "By title, Ascending": 1,
  "By title, Descending": 2,
  "By author, Ascending": 3,
  "By author, Descending": 4,
  "By release date, Ascending": 5,
  "By release date, Descending": 6,
  "By price, Ascending": 7,
  "By price, Descending": 8
}


def book_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    cart_book_form = CartAddProductForm()
    search_form = SearchBar
    sort_choices = SortChoices
    sort_choice = None
    if request.method == "POST":
      form = SortChoices(request.POST)
      if form.is_valid():
        cd = form.cleaned_data
        sort_choice = cd['choice']

    if sort_choice == 1:
      books = Book.objects.filter(available=True).order_by('title')[::-1]
    elif sort_choice == 2:
      books = Book.objects.filter(available=True).order_by('title')
    elif sort_choice == 3:
      books = Book.objects.filter(available=True).order_by('authors__last_name')[::-1]
    elif sort_choice == 4:
      books = Book.objects.filter(available=True).order_by('authors__last_name')
    elif sort_choice == 5:
      books = Book.objects.filter(available=True).order_by('publication_date')[::-1]
    elif sort_choice == 6:
      books = Book.objects.filter(available=True).order_by('publication_date')
    elif sort_choice == 7:
      books = Book.objects.filter(available=True).order_by('price')[::-1]
    elif sort_choice == 8:
      books = Book.objects.filter(available=True).order_by('price')
    else:
      books = Book.objects.filter(available=True)
      
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    return render(request, 'books/book/list.html', {'genre': genre,
                                                      'genres': genres,
                                                      'books': books,
                                                      'cart_book_form': cart_book_form,
                                                      'search_form': search_form,
                                                      'sort_choices': sort_choices})


def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_book_form = CartAddProductForm()
    return render(request,
                  'books/book/detail.html',
                   {'book': book,
                    'cart_book_form': cart_book_form})
