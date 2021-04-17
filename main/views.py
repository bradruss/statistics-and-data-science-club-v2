from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def people(request):
    return render(request, 'main/people.html')

def software(request):
    return render(request, 'main/software.html')

def links(request):
    return render(request, 'main/links.html')

def asa(request):
    return render(request, 'main/asa.html')

def career_resources(request):
    return render(request, 'main/career_resources.html')

#def contact(request):
#    return render(request, 'main/contact.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
			'first_name': form.cleaned_data['first_name'],
			'last_name': form.cleaned_data['last_name'],
			'email': form.cleaned_data['email_address'],
			'message':form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/success/")

	form = ContactForm()
	return render(request, "main/contact.html", {'form':form})

def success(request):
    return render(request, 'main/success.html')

def handler404(request, *args, **kwargs):
    return render(request, 'main/404.html', status=404)

def handler500(request):
    return render(request, 'main/500.html', status=500)
