from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Post
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Create your views here.
def index(request):
    # Import Post models/objects into index.html
    time = timezone.now()
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts, 'time': time})

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
            send_email  = EmailMessage(
                subject = "Website Inquiry",
                to=[SECRET_EMAIL],
                from_email=user_email,
                reply_to=[user_email],
                body = message,
                headers = "Header"
                )

            '''# Send email via normal mode
            try:
                send_mail(subject, message, user_email, [SECRET_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # Below is the SendGrid code, commented out now for testing
            '''

            # Send email via SendGrid
            try:
                # Try to send it via SendGrid
                # send_email.send(fail_silently="Oh god it broke")

                # Old method
#                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#                response = sg.send(send_email)
                response = send_email.send(fail_silently="Oh god it broke")
                print(response)

            except Exception as e:
                # If failed, print msg to console
                print(e)

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

#def post_list(request):

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})