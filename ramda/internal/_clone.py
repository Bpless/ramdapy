import copy


def _clone(value):
    '''
    Performs deep copy of an object.
        @private

    The semantics for _clone in ramda.js are the following:
        Recursively copy (possibly nested) properties from
        objects of types `Object`, `Array`, `Date`, `Regex`,
        and other (catchall). In the case of `Regex`,
        perform a custom copy via `_cloneRegExp`.
        `Function`s are not copied, but assigned by their reference,
        via deep equality testing.

    For the initial implementation of this _clone, we will alias
    Python's copy module. That library is presumably written in C
    and highly optimized.

    In certain versions of Python,
    this will cause objects with compiled regex properties to
    throw (http://bugs.python.org/issue10076).

    Longterm, it may make sense to implementat deepcopy here
    as a regex "safe" deepcopy in that library users can already
    access the Python copy module directly, making this an
    alternative option.
    '''
    return copy.deepcopy(value)
