from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_email, validate_password, validate_first_name, validate_last_name
from django.core.validators import EmailValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    """
    Override standard user model fields by adding custom validators
    """
    email = models.EmailField('email address', blank=False, validators=[EmailValidator, validate_email])
    password = models.CharField('password', max_length=128, validators=[validate_password])
    first_name = models.CharField('first name', max_length=150, blank=True, validators=[validate_first_name])
    last_name = models.CharField('last name', max_length=150, blank=True, validators=[validate_last_name])


class RegistrationRequest(models.Model):
    """
    This model for logging registration request
    """
    email = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    This signal create Token for user after custom user model is created
    """
    if created:
        Token.objects.create(user=instance)
