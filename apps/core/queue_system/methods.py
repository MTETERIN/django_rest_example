from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
from django.utils.html import strip_tags


class ConsumerMethods(object):
    body = None

    @classmethod
    def send_email(cls):
        """
        Send an email message.
        :return:
        """
        template = cls.body['template']
        subject = cls.body['subject']
        to = cls.body['to']
        from_email = cls.body['from_email']
        context = cls.body['context']
        context = Context(context)

        html_message = get_template('email/' + template + '.html').render(context)
        message = strip_tags(html_message)

        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to,
            html_message=html_message
        )
