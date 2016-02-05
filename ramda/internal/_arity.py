from functools import wraps


def _arity(n, fn):
    '''
    This function is utilized by ramdajs to enforce
    fixed length argument signatures.

    It is not clear if it will actually be of worth in Python.
    ramdajs similiarly limits itself to length of 9 args.

    We could potentially use a eval here to dynamically define
    functions via string templates.
    '''
    try:
        return wraps(fn, [
            lambda: fn(),
            lambda a0: fn(a0),
            lambda a0, a1: fn(a0, a1),
            lambda a0, a1, a2: fn(a0, a1, a2),
            lambda a0, a1, a2, a3: fn(a0, a1, a2, a3),
            lambda a0, a1, a2, a3, a4: fn(a0, a1, a2, a3, a4),
            lambda a0, a1, a2, a3, a4, a5: fn(
                a0, a1, a2, a3, a4, a5
            ),
            lambda a0, a1, a2, a3, a4, a5, a6: fn(
                a0, a1, a2, a3, a4, a5, a6
            ),
            lambda a0, a1, a2, a3, a4, a5, a6, a7: fn(
                a0, a1, a2, a3, a4, a5, a6, a7
            ),
            lambda a0, a1, a2, a3, a4, a5, a6, a7, a8: fn(
                a0, a1, a2, a3, a4, a5, a6, a7, a8
            )
        ][n])
    except IndexError:
        raise ValueError(
            'First argument to _arity must be a non-negative integer < ten'
        )
