def _aperture(n, _iter):
    limit = len(_iter) - n + 1
    return [_iter[i:i + n] for i in xrange(limit if limit >= 0 else 0)]
