import re

from django.core.exceptions import ValidationError


def phone_validator(phone):
    conditions = [
        not phone[1:].isdigit(),
        phone[0] != '+',
        len(phone) != 12
    ]
    if any(conditions):
        raise ValidationError('Поле должно быть формата +79876543211')


def validate_password(value):
    pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!.%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    if re.match(pattern1, value):
        return value
    else:
        raise ValidationError('Пароль должен быть не менее 8 символов, только латиница, минимум 1 '
                              'символ верхнего регистра, минимум 1 спец символ')