from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TagForm
from quotes.models import Quote


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='tags:tag')
        else:
            return render(request, 'tags/tag.html', {'form': form})

    return render(request, 'tags/tag.html', {'form': TagForm()})


def quotes_by_tag(request, tagname):
    quotes_by_tag = Quote.objects.filter(tags__name=tagname)
    return render(request, 'tags/quotes_by_tag.html', context={'quotes_by_tag': quotes_by_tag, 'tag':tagname})