from functools import wraps

from ramda.internal._placeholder import __
from ramda.internal._curry1 import _curry1


def _curry2(fn):
    '''
    Optimized internal two-arity curry function.
     @private
     @category Function
     @param {Function} fn The function to curry.
     @return {Function} The curried function.
    '''
    @wraps(fn)
    def inner(*args):
        arg_count = len(args)
        if arg_count == 0 or arg_count == 1 and args[0] is __:
            return inner
        elif arg_count == 1:
            return _curry1(lambda _b: fn(args[0], _b))
        elif args[0] is __ and args[1] is __:
            return inner
        elif args[0] is __:
            return _curry1(lambda _b: fn(args[1], _b))
        elif args[1] is __:
            return _curry1(lambda _b: fn(args[0], _b))
        else:
            return fn(*args)
    return inner
