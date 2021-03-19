from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
	surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
	date = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
	tel_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
	class Meta:
		model = Contact
		fields = [
			"name",
			"surname",
			"date",
			"tel_number"
		]