from ramda.internal._curry2 import _curry2


def _reps_positive_int(s):
    try:
        return int(s) >= 0
    except ValueError:
        return False


@_curry2
def _has(key, obj):
    '''
    The semantics for _has in ramda.js are the following:
    perform a hasOwnProperty call against an object
    of varying types.  This means that
           _has('0', [10]) => true
       _has('1', [10]) => false
       _has('name', {name: 'Arnold'}) => true
       _has('name', instanceFromConstructor) => true
       _has('2', 'the') => true
        To achieve this in python, we perform some
    (potentially) non-exhaustive type checks.

    The catchall at the bottom works for objects at large
    but may be too broad.  Perhaps we should error with certain
    input types.
    '''
    if hasattr(obj, '__len__') and _reps_positive_int(key):
        return key < obj.__len__()
    elif isinstance(obj, dict):
        return key in obj
    else:
        return hasattr(obj, key)
