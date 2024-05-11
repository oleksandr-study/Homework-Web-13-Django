from django.urls import path

from . import views


app_name = "tags"

urlpatterns = [
        path('tag/', views.tag, name='tag'),         #tags:tag
        path('<str:tagname>', views.quotes_by_tag, name='quotes_by_tag'),         #tags:quotes_by_tag
]