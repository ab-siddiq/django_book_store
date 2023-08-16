from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.
def home(request):
    return render(request,'view_book.html')

def store_book(request):
    book = BookStoreForm(request.POST)
    if book.is_valid():
        book.save()
        print(book.cleaned_data)
        return redirect("show_books")
    else:
        book = BookStoreForm()
        return render(request,'store_book.html',{'form':book})
def show_books(request):
    book = BookStoreModel.objects.all()
    return render(request,'show_books.html',{'books':book})

def edit_book(request,id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    return render(request, 'store_book.html',{'form':form})
def delete_book(request,id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('show_books')