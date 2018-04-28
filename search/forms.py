from django import forms

SORT_CHOICES = [(1, "By title, Ascending"), (2, "By title, Descending"), 
				(3, "By author, Ascending"), (4, "By author, Descending"),
				(5, "By release date, Ascending"), (6, "By release date, Descending"), 
				(7, "By price, Ascending"), (8, "By price, Descending")]

class SearchBar(forms.Form):
	phrase = forms.CharField(max_length=30)

class SortChoices(forms.Form):
    choice = forms.TypedChoiceField(choices=SORT_CHOICES,
    								coerce=int)

