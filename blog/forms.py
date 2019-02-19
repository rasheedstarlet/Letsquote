from django import forms

from . models import Quote
class QuoteCreationForm(forms.ModelForm):

	class Meta:
		model = Quote
		fields = [
		'body',
		'writer',
		]