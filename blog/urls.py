from django.urls import path

from . import views

from blog.views import QuoteList

app_name = 'blog'

urlpatterns = [
    path('', QuoteList.as_view(), name="quotes"),
    path('create', views.QuoteCreationView, name="create"),
]
