# -*- coding: utf-8 -*-


QUEUE_SETTINGS = {
    'EXCHANGE_NAME': 'django_rest_example',
    'EXCHANGE_TYPE': 'topic'
}

ROUTING_KEYS = {
    'default_consumer': {
        'core.send_email': ['send_email', ],
    },
}
