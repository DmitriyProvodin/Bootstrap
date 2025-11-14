from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def validate_no_external_links(value):
    if not value:
        return
    parsed = urlparse(value)
    host = parsed.netloc.lower()
    if 'youtube' in host or 'youtu.be' in host:
        return
    raise ValidationError('External links are forbidden - only YouTube allowed.')
