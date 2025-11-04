from django.core.exceptions import ValidationError
from urllib.parse import urlparse


def validate_no_external_links(value):
    if not value:
        return
    try:
        parsed = urlparse(value)
        host = parsed.netloc.lower()
        if ':' in host:
            host = host.split(':')[0]
        if 'youtube' in host or 'youtu.be' in host:
            return
        raise ValidationError('Ссылки на внешние ресурсы запрещены — допустим только YouTube.')
    except Exception:
        raise ValidationError('Недопустимый URL.')
