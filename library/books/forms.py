from django import forms
from books.models import Book

# class BookForm(forms.ModelForm):
#     class Meta:
#         model=Book
#         fields=['title','price']

class BookForm(forms.ModelForm):
     class Meta:
         model = Book
         fields = "__all__"


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         exclude="__all__"




