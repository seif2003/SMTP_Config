from django.db import models

class SMTPConfig(models.Model):
    EMAIL_HOST = models.CharField(max_length=100)
    EMAIL_PORT = models.IntegerField()
    EMAIL_HOST_USER = models.EmailField()
    EMAIL_HOST_PASSWORD = models.CharField(max_length=100)
    # Company 1 to 1 relation