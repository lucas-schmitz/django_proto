import os
from django.db.models.fields.files import FieldFile
from django.core.exceptions import ValidationError


def is_python(path):
    if isinstance(path, FieldFile):
        path = path.name
    head, tail = os.path.split(path)
    if not tail.endswith(".py"):
        raise ValidationError(u'Must be a python file.')
    else:
        return True
