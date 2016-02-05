import functools


def partial(fn, *args, **kwargs):
    return functools.partial(fn, *args, **kwargs)
