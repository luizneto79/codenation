from django.core.exceptions import ValidationError


def validate_level(value):
    levels = ('CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO')

    if value not in levels:
        raise ValidationError('O valor não está entre as opções (CRITICAL, '
                              'DEBUG, ERROR, WARNING, INFO)')
