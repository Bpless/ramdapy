import types


def _isArray(obj):
    '''
    Tests whether or not an object is an array.

    The semantics are a bit different than ramdaJS in that
    we are treating generators, tuples, and lists as interchangeable,
    for the sake of this internal function.

    @private
    @param {*} val The object to test.
    @return {Boolean} `true` if `val` is an array, `false` otherwise.
    @example

        _isArray([]); //=> true
        _isArray(null); //=> false
        _isArray({}); //=> false
    '''
    _types = [list, tuple, types.GeneratorType]
    return any([True if isinstance(obj, _type) else False for _type in _types])
