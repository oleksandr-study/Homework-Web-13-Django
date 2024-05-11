from django.urls import path

from . import views


app_name = "authors"

urlpatterns = [
    path('add_author/', views.add_author, name='add_author'),      #authors:add_author
    path('author/<int:author_id>', views.author_details, name='author_details'),      #authors:author_details
]