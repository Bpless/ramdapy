from ramda.internal import _curry3


@_curry3
def adjust(fn, idx, _iter):
    '''
    Applies a function to the value at the given index of an iterable,
    returning a new copy of the array with the element at the given
    index replaced with the result of the function application.
    '''
    return (el if i != idx else fn(el) for i, el in enumerate(_iter))
