from ramda.internal import _curry2


@_curry2
def _and(a, b):
    '''
    Adds two values.
        R.add(2, 3);       //=>  5
        R.add(7)(10);      //=> 17
    '''
    return a and b
