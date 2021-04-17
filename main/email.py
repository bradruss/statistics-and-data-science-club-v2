from django.core.mail import send_mail
from django.http import HttpResponse

def

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret email used in production secret!
with open(os.path.join(BASE_DIR, '../secret_email.txt')) as f:
    SECRET_EMAIL = f.read().strip()

# Send email to secret address
send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    [SECRET_EMAIL],
    fail_silently=False,
)