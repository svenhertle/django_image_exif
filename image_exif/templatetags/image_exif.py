from django import template
from django.core.exceptions import MultipleObjectsReturned

from image_exif.models import ExifData

register = template.Library()

@register.assignment_tag
def exif(image):
    # try database
    try:
        return ExifData.objects.get(image=image)
    # else create
    except ExifData.DoesNotExist as e:
        obj = ExifData(image=image)
        obj.save()

        return obj
    except MultipleObjectsReturned as e:
        return {}
