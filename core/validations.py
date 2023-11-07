import re
from django.forms import ValidationError


def validate_email(value):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    if not re.match(email_pattern, value):
        raise ValidationError("Invalid email format")
