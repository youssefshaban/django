from django.shortcuts import render, redirect

# Create your views here.
from .form import BookForm
from .models import bookStore


def index(request):
    books = bookStore.objects.all()
    return  render(request,'bookStore/index.html',{
        'books': books
    })


def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'bookStore/create.html',{
        'form': form
    })


def edit(request, id):
    book = bookStore.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'bookStore/edit.html', {
        'form': form,
        'book': book
    })


def delete(request, id):
    book = bookStore.objects.get(pk=id)
    book.delete()
    return redirect('index')