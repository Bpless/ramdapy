from functools import wraps

from ramda.internal._placeholder import __


def _curry1(fn):
    '''
    Optimized internal one-arity curry function.
     @private
     @category Function
     @param {Function} fn The function to curry.
     @return {Function} The curried function.

    Used internally to require that functions which
    depend on a single argument (i.e. curry)
    are either called with an argument or return themselves
    '''
    @wraps(fn)
    def inner(*args):
        arg_count = len(args)
        if arg_count == 0 or args[0] is __:
            return inner
        else:
            return fn(*args)
    return inner
