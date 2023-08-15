from django.shortcuts import render,redirect
from book.forms import BookStoreForm
# Create your views here.
def home(request):
    return render(request,'view_book.html')

def store_book(request):
    book = BookStoreForm(request.POST)
    if book.is_valid():
        # book.save()
        print(book.cleaned_data)
        return redirect("show_books")
    return render(request,'store_book.html',{'form':book})
def view_book(request):
    form = BookStoreForm
    return render(request,'view_book.html',{'form':form})