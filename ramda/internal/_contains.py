from ramda.internal._indexOf import _indexOf


def _contains(a, _iter):
    return _indexOf(_iter, a) >= 0
