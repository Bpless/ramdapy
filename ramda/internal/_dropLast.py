from ramda.internal._take import _take


def _dropLast(n, _iter):
    length = len(_iter)
    return _take(length - n if n < length else 0, _iter)
