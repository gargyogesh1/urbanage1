import re
from django.core.exceptions import ValidationError

def is_basic_valid_indian_number(phone_number):
    pattern = re.compile(r'^[6-9]\d{9}$')
    if not pattern.match(phone_number):
        raise ValidationError('Enter a valid 10-digit Indian phone number starting with 6, 7, 8, or 9.')
