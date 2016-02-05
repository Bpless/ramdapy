from ramda.internal._filter import _filter


def _functionsWith(fn):
    '''
    @private
    @param {Function} fn
        Strategy for extracting function names from an object
    @return {Function}
        function that takes an object and returns an array of function names.
    '''
    def inner(obj):
        return _filter(lambda prop: callable(getattr(obj, prop)), fn(obj))
    return inner
