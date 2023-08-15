from django import forms
from book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        # fields = ['id','book_name','author','edition','category']
        exclude = ['publication_date','last_published']