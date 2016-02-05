from functools import reduce

from ramda.internal._curry3 import _curry3


# For backwards compatibility, we rely on
# functools.reduce instead of deprecated reduce.
_reduce = _curry3(reduce)
