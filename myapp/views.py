# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SMTPConfig
from .serializers import SMTPConfigSerializer
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

@api_view(['POST'])
def create_smtp_config(request):
    """
    {
        "EMAIL_HOST":"smtp.gmail.com",
        "EMAIL_PORT":"587",
        "EMAIL_HOST_USER":"xxxxx@gmail.com",
        "EMAIL_HOST_PASSWORD":"xxxx yyyy zzzz xxxx"
    }
    """
    if request.method == 'POST':
        serializer = SMTPConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_email(subject, message, recipient_emails):

    smtp_config = SMTPConfig.objects.first() # TODO CHANGE THIS !!!!!! raquest.user.company.SMTPConfig

    # Create a new EmailBackend instance with the SMTP settings
    email_backend = EmailBackend(
        host=smtp_config.EMAIL_HOST,
        port=smtp_config.EMAIL_PORT,
        username=smtp_config.EMAIL_HOST_USER,
        password=smtp_config.EMAIL_HOST_PASSWORD,
        use_tls=True
    )

    # Create the email message
    email = EmailMessage(
        subject,
        message,
        smtp_config.EMAIL_HOST_USER,
        recipient_emails,
        connection=email_backend
    )

    # Send the email
    email.send()

@api_view(['POST'])
def send_email_view(request):
    """
    {
        "subject":"hello",
        "message":"hello",
        "recipient_emails":["xxxxxxxx@gmail.com","yyyyyyyyy@gmail.com"]
    }
    """
 
    if request.method == 'POST':
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_emails = request.data.get('recipient_emails')
        send_email(subject, message, recipient_emails)
        return Response(status=status.HTTP_200_OK)