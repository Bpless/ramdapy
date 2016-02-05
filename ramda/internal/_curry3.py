from functools import wraps

from ramda.internal._placeholder import __
from ramda.internal._curry1 import _curry1
from ramda.internal._curry2 import _curry2


def _curry3(fn):
    '''
    Optimized internal three-arity curry function.
     @private
     @category Function
     @param {Function} fn The function to curry.
     @return {Function} The curried function.
    '''

    wrapper = wraps(fn)

    @wrapper
    def inner(*args):
        arg_count = len(args)
        if arg_count == 0:
            return inner
        elif arg_count == 1:
            if args[0] is __:
                return inner
            else:
                return _curry2(wrapper(lambda _b, _c: fn(args[0], _b, _c)))
        elif arg_count == 2:
            if args[0] is __ and args[1] is __:
                return inner
            elif args[0] is __:
                return _curry2(wrapper(lambda _b, _c: fn(args[1], _b, _c)))
            elif args[1] is __:
                return _curry2(wrapper(lambda _b, _c: fn(args[0], _b, _c)))
            else:
                return _curry1(wrapper(lambda _c: fn(args[0], args[1], _c)))
        else:
            if args[0] is __ and args[1] is __ and args[2] is __:
                # All three arguments are placeholders, star again.
                return inner
            elif args[1] is __ and args[2] is __:
                # Only the first argument is non-placeholder, curry remaining
                return _curry2(wrapper(lambda _b, _c: fn(args[0], _b, _c)))
            elif args[2] is __:
                # The first and second arguments are non-placeholders,
                # curry the third argument.
                return _curry1(wrapper(lambda _c: fn(args[0], args[1], _c)))
            elif args[1] is __:
                # The first and third arguments are non-placeholders,
                # curry the second argument.
                return _curry1(wrapper(lambda _b: fn(args[0], _b, args[2])))
            elif args[0] is __ and args[2] is __:
                # Only the second argument is non-placeholder,
                # curry the first and third arguments.
                return _curry2(wrapper(lambda _a, _c: fn(_a, args[1], _c)))
            elif args[0] is __:
                # The second and third arguments are non-placeholders,
                # curry the first argument
                return _curry1(wrapper(lambda _a: fn(_a, args[1], args[2])))
            elif args[0] is __ and args[1] is __:
                # Only the third argument is a placeholder,
                # curry the first and second arguments
                return _curry2(wrapper(lambda _a, _b: fn(_a, _b, args[2])))
            else:
                # Three non-placeholder values discovered, apply function
                return fn(*args)
    return inner
