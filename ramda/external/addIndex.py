from ramda.external import _curry2, _concat


@_curry2
def addIndex(fn):
    '''
    DOES NOT WORK
    '''
    args_clone = args[:]
    original_fn = args_clone[0]
    _iter = args_clone[-1]
    idx = 0

    def wrapped_fn(*args):
        result = original_fn(*_concat(args, [idx, _iter]))
        idx += 1
        return result

    def inner(*args):
        args_clone[0] = wrapped_fn
        return fn(*args)

    return _curryN(len(inspect.getargspec(fn).args), inner)
