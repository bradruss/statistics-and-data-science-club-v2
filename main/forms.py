from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50, required = True)
	last_name = forms.CharField(max_length = 50, required = True)
	email_address = forms.EmailField(max_length = 150, required = True)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000, required = True)