from functools import wraps


def _curryN(length, fn, received=None):
    '''
    Internal curryN function.

    @private
    @category Function
    @param {Number} length The arity of the curried function.
    @param {Function} fn The function to curry.
    @param {Array} received An array of arguments received thus far.
    @return {Function} The curried function with a new
    arity function signature (i.e. fn(a0, a1)).

    As it stands, this is less efficient than the Node
    version and also has to deal with the fact that
    extra arguments are expected in the Node version,
    while function signatures in Python are more strict
    about argument number.  So, seeing extra args in this
    case would be confusing for a Python developer.

    We could potentially preserve the names of the original
    arguments using the inspect module.

        @curry(length=2)
        def add_to_cart(cart_id, item):
            pass

        add_to_cart_five = add_to_cart(5)
        print inspect.getargspec(add_to_cart_five).args
            > item
    '''
    from ramda.internal import __

    received = received or [__] * length

    @wraps(fn)
    def inner(*args):
        received_clone = received[:]
        slot_index = 0
        non_placeholder_args = [a for a in args if a != __]
        for i, arg in enumerate(non_placeholder_args):
            if slot_index >= length:
                raise TypeError(
                    '{} takes exactly {} arguments ({} given)'.format(
                        fn, length, length + len(non_placeholder_args) - i
                    )
                )
            else:
                while slot_index < length:
                    slot = received_clone[slot_index]
                    if slot is __:
                        received_clone[slot_index] = arg
                        slot_index += 1
                        break
                    else:
                        slot_index += 1

        left = sum([1 for _slot in received_clone if _slot is __])
        if left:
            return _curryN(length, fn, received_clone)
        else:
            return fn(*received_clone)
    return inner
