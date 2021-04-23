from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .form import BookForm, CatForm
from .models import bookStore
from .form import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request, "bookStore/register.html", {"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "bookStore/login.html", {"login_form": form})


@login_required(login_url='login')
def index(request):
    books = bookStore.objects.all()
    return render(request, 'bookStore/index.html', {
        'books': books
    })


def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'bookStore/create.html', {
        'form': form
    })


@login_required(login_url='login')
@permission_required('can add category', login_url='login')
def createCat(request):
    form = CatForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'bookStore/createCat.html', {
        'form': form
    })


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete(request, id):
    book = bookStore.objects.get(pk=id)
    book.delete()
    return redirect('index')
