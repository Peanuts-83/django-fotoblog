from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError

#  Password validator : 1 letter ++
class WithLettersValidator:
    def validate(self, password, usr=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Password must contain at least one letter', 'pwd_no_letter')

    def get_help_text(self):
        return 'Your password must contain at least one letter, uppercase or lowercase.'

#  Password validator : 1 number ++
class WithNumbersValidator:
    def validate(self, password, usr=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain at least a number', 'pwd_no_number')

    def get_help_text(self):
        return 'Your password must contain at least a number.'