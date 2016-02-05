from ramda.internal import _pipe, _reduce


def pipe(*args):
    '''
    Performs left-to-right function composition. The leftmost function may have
    any arity; the remaining functions must be unary.
    In some libraries this function is named `sequence`.
    @func
    @memberOf R
    @since v0.1.0
    @category Function
    @sig (((a, b, ..., n) -> o), (o -> p), ..., (x -> y), (y -> z)) -> ((a, b, ..., n) -> z)
    @param {...Function} functions
    @return {Function}
    @see R.compose
    @example
       var f = R.pipe(Math.pow, R.negate, R.inc);
       f(3, 4); // -(3^4) + 1

    '''
    if (len(args) == 0):
        raise TypeError('pipe requires at least one argument')
    else:
        return _reduce(_pipe, args[1:], args[0])
