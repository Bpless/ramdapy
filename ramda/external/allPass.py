import inspect

from ramda.internal import _curryN


def allPass(preds):
    '''
    '''
    arity = max([len(inspect.getargspec(pred).args) for pred in preds])

    def inner(*args):
        for fn in preds:
            if not fn(*args):
                return False
        return True
    return _curryN(arity, inner)
