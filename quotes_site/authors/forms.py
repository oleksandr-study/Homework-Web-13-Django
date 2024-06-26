from django.forms import ModelForm, CharField, TextInput
from quotes.models import Author


class AuthorForm(ModelForm):

    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_location = CharField(min_length=5, max_length=150, required=True, widget=TextInput())
    description = CharField(min_length=5, required=True, widget=TextInput())
    
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']