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

    # Code for sending an email using the data in the form via SendGrid
    if request.method == 'POST':

        # Get form data after submit
        form = ContactForm(request.POST)

        if form.is_valid():

            # Email subject
            subject = "Website Inquiry"

            # Get the data from each field
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email_address'],
            'message':form.cleaned_data['message'],
            }

            # Combine field data into one string
            message = "\n".join(body.values())

            # Get email address from body dict
            user_email = body.get('email')

            # Get email address to send to via os.path
            # IMPORTANT: KEEP SECRET EMAIL A SECRET!!!!
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            with open(os.path.join(BASE_DIR, '../secret_email.txt')) as f:
                SECRET_EMAIL = f.read().strip()

            # Create mail object
            msgToSend = Mail(
                from_email=user_email,
                to_emails=SECRET_EMAIL,
                subject='Sending with Twilio SendGrid is Fun',
                html_content='<strong>' + message + '</strong>'
                )

            # Below is the SendGrid code, commented out now for testing
            '''try:
                echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
                echo "sendgrid.env" >> .gitignore
                source ./sendgrid.env

                # Try to send it via SendGrid
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(msgToSend)
                print(response.status_code)
                print(response.body)
                print(response.headers)

            except Exception as e:
                # If failed, print msg to console
                print(e.message)'''

            # If it works, go to success page.
            return redirect ("/success/")

    form = ContactForm()
    return render(request, "main/contact.html", {'form':form})

def success(request):
    return render(request, 'main/success.html')

def handler404(request, *args, **kwargs):
    return render(request, 'main/404.html', status=404)

def handler500(request):
    return render(request, 'main/500.html', status=500)
