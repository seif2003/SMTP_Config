# urls.py
from django.urls import path
from .views import create_smtp_config, send_email_view

urlpatterns = [
    path('api/smtp-config/', create_smtp_config, name='create_smtp_config'),
    path('api/send-email/', send_email_view, name='send_email'),
]
