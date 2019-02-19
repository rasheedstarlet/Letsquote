from django.shortcuts import render, HttpResponse, redirect, reverse

from . models import Quote

from . forms import QuoteCreationForm

from django.views.generic.list import ListView


'''
def QuoteList(request):
    quotes = Quote.objects.all().order_by('-created_date')
    return render(request, 'blog/quotelist.html', {'quotelist': quotes })
'''

def QuoteCreationView(request):
 if request.method == "POST":
 	form = QuoteCreationForm(request.POST)
 	if form.is_valid():
 		form.save()
 		return redirect('blog:quotes')
 	else:
 		return redirect('blog:create')
 else:
 	form = QuoteCreationForm()
 return render(request, 'blog/create_quote.html', {'form':form })


class QuoteList(ListView):
	model = Quote
	paginate_by = 5
	template_name = 'blog/quotelist.html'
	context_object_name = 'quotelist'