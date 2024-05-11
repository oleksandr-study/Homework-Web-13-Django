from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm
from quotes.models import Author

# Create your views here.
# from .utils import get_mongodb
# from .forms import TagForm


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='authors:add_author')
        else:
            return render(request, 'authors/add_author.html', {'form': form})
    return render(request, 'authors/add_author.html', {'form': AuthorForm()})


def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authors/authors_page.html', context={'author': author})