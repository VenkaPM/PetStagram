from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            #invalid case
            raise ValidationError('Value must contain only letters')
    #valid case


def validate_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))
    return validate