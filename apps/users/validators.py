from apps.users.utils import is_invalid_password


def check_valid_password(data):
    """
    Password validation.
    :param data:
    """
    invalid_password_message = is_invalid_password(data.get('password'), data.get('repeat_password'))

    if invalid_password_message:
        raise invalid_password_message
