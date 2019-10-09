import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            u'Upload a valid image. The file you uploaded was either not an image or a corrupted image.')
