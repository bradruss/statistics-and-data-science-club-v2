from django import forms

# Code source: https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    