from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm
from .models import Quote, Tag, Author

# Create your views here.


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


@login_required
def add_quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            new_quote.author = Author.objects.filter(fullname=request.POST.get('authors')).first()
            new_quote.save()

            return redirect(to='quotes:add_quote')
        else:
            return render(request, 'quotes/add_quote.html', {"authors": authors, "tags": tags, 'form': form})

    return render(request, 'quotes/add_quote.html', {"authors": authors, "tags": tags, 'form': QuoteForm()})