from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv


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


#            load_dotenv()

 #           MY_ENV_VAR = os.getenv('MY_ENV_VAR')

            message = Mail(
                from_email='from_email@example.com',
                to_emails='to@example.com',
                subject='Sending with Twilio SendGrid is Fun',
                html_content='<strong>and easy to do anywhere, even with Python</strong>')
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
#                print(e.message)
                print("e")

            '''subject = "Website Inquiry"

            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email_address'],
            'message':form.cleaned_data['message'],
            }

            message = "\n".join(body.values())

            email_from_form = body.get('email')

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            with open(os.path.join(BASE_DIR, '../secret_email.txt')) as f:
                SECRET_EMAIL = f.read().strip()

            message = Mail(
                from_email=email_from_form,
                to_emails=SECRET_EMAIL,
                subject='Sending with Twilio SendGrid is Fun',
                html_content='<strong>' + message + '</strong>'
                )

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)'''

            return redirect ("/success/")

    form = ContactForm()
    return render(request, "main/contact.html", {'form':form})

def success(request):
    return render(request, 'main/success.html')

def handler404(request, *args, **kwargs):
    return render(request, 'main/404.html', status=404)

def handler500(request):
    return render(request, 'main/500.html', status=500)
