from django.core.exceptions import ValidationError
import re


def validate_email(email):
    """
    length less then 100 symbols.
    Check forbidden email providers.
    """
    forbidden_email = ['@gmail.com', '@icloud.com']

    if len(email) > 100:
        raise ValidationError('length more then 100 symbols')

    for provider in forbidden_email:
        if re.search(f'{provider}', email):
            raise ValidationError('Forbidden provider')


def validate_first_name(first_name):
    """
    Only letters and hyphens
    """
    if re.match(r'^[a-z\-]+$', first_name) is None:
        raise ValidationError('Only letters and hyphens')


def validate_last_name(last_name):
    """
    Only letters, hyphens and white spaces
    """
    if re.match(r'^[a-z\-\s]+$', last_name) is None:
        raise ValidationError('Only letters, hyphens and white spaces')


def validate_password(password):
    """
    Only letters, digits, underscore. Starts with capital letter. length from 7 to 16 symbols.
    """
    if not 7 <= len(password) <= 16:
        raise ValidationError('length from 7 to 16 symbols')
    if re.match(r'^[a-zA-Z\d_]+$', password) is None:
        raise ValidationError('Only letters, digits, underscore')
    if not password[0].isupper():
        raise ValidationError('Must starts with capital letter')
