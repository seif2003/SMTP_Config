# serializers.py
import smtplib
from rest_framework import serializers
from .models import SMTPConfig

class SMTPConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMTPConfig
        fields = ['id', 'EMAIL_HOST', 'EMAIL_PORT', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD']
        
    def validate(self, data):
        email_host = data.get('EMAIL_HOST')
        email_port = data.get('EMAIL_PORT')
        email_host_user = data.get('EMAIL_HOST_USER')
        email_host_password = data.get('EMAIL_HOST_PASSWORD')

        # Attempt to connect to the SMTP server and login
        try:
            with smtplib.SMTP(email_host, email_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(email_host_user, email_host_password)
        except Exception as e:
            raise serializers.ValidationError("SMTP configuration is invalid. Error: {}".format(str(e)))

        return data
