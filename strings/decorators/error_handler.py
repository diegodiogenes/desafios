import logging


def error_handler(func):
    """
    decorator to handle File Not Found exception
    :param func:
    :return:
    """
    def handler(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileNotFoundError as e:
            raise Exception(logging.error(f"{func.__name__} -- FileNotFoundError: {e}"))
    return handler
