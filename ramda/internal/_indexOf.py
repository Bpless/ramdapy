from ramda.internal._equals import _equals


def _indexOf(_iter, comp):
    '''
    In this implementation, as compared to ramdajs,
    we are ignoring the distinction between +0 and -0.

    We could delegate to `index` method for `Array`
    and `String` type but that is not compatible with
    generators.
    '''
    for i, element in enumerate(_iter):
        if _equals(element, comp):
            return i
    return -1
