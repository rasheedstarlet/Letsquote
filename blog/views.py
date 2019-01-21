from django.shortcuts import render, HttpResponse

from . models import Quote

def QuoteList(request):
    quotes = Quote.objects.all()
    return render(request, 'blog/quotelist.html', {'quotelist': quotes })
