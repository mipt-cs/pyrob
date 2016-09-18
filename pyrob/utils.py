#!/usr/bin/python3

import sys
import functools

def log_invocation(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        logger = sys.modules[f.__module__].logger
        logger.debug('Calling function {} with arguments: args={}, kwargs={}'.format(f.__name__, args, kwargs))
        ret = f(*args, **kwargs)
        logger.debug('Return value of {} is {}'.format(f.__name__, ret))
        return ret

    return wrapper


class AllowInternalContext:

    allow_internal = False

    @classmethod
    def internal_allowed(cls):
        return cls.allow_internal

    def __init__(self, allow):
        self.flag = self.allow_internal
        self.allow = allow

    def __enter__(self):
        self.allow_internal = self.allow

    def __exit__(self, *args):
        self.allow_internal = self.flag


def allow_internal(flag):
    return AllowInternalContext(flag)


def internal(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if AllowInternalContext.allow_internal:
            raise NotImplementedError("API {} is marked as internal".format(f.__name__))
        return f(*args, **kwargs)

    return wrapper


def public(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        with allow_internal(True):
            return f(*args, **kwargs)

    return wrapper


def repeat(n, f, *args, **kwargs):
    assert n > 0
    for i in range(n):
        f(*args, **kwargs)