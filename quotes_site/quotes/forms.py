from django.forms import ModelForm, CharField, TextInput
from .models import Quote


class QuoteForm(ModelForm):

    quote = CharField(min_length=5, required=True, widget=TextInput())
    
    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['author', 'tags']