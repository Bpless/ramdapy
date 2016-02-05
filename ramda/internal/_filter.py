from ramda.internal._curry2 import _curry2

_filter = _curry2(lambda fn, _iter: (x for x in _iter if fn(x)))
