import hashlib
import random
import string

from django.conf import settings

from apps.core.queue_system.publisher import BasePublisher


def generate_unique_key(value, length=40):
    """
    generate key from passed value
    :param value:
    :param length: key length
    :return:
    """

    salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(26)).encode(
        'utf-8')
    value = value.encode('utf-8')
    unique_key = hashlib.sha1(salt + value).hexdigest()

    return unique_key[:length]


def send_email_job(to, template, context, subject):
    """
    Create a new email job for queue.
    :param to:
    :param template:
    :param context:
    :param subject:
    """
    from_email = settings.SENDER_EMAIL
    to_email = [to]

    context['client_side_url'] = settings.CLIENT_BASE_URL

    # Publishing a new email job
    BasePublisher(
        routing_key='core.send_email',
        body={
            'context': context,
            'to': to_email,
            'from_email': from_email,
            'template': template,
            'subject': subject,
        }
    )
