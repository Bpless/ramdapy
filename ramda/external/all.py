from ramda.internal import _curry2


@_curry2
def all(fn, _iter):
    '''
    Returns `True` if all elements of the list match the predicate,
    False if there are any that don't.

    TODO: name ambiguity with python builtin all.
    '''
    for el in _iter:
        if not fn(el):
            return False
    return True
