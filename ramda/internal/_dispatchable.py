from ramda.internal._isArray import _isArray


def _dispatchable(methodname, xf, fn):
    '''
    Returns a function that dispatches with different strategies based on the
    object in list position (last argument). If it is an array, executes [fn].
    Otherwise, if it has a function with [methodname], it will execute that
    function (functor case). Otherwise, if it is a transformer, uses transducer
    [xf] to return a new transformer (transducer case). Otherwise, it will
    default to executing [fn].
    @private
    @param {String} methodname property to check for a custom implementation
    @param {Function} xf transducer to initialize if object is transformer
    @param {Function} fn default ramda implementation
    @return {Function} A function that dispatches on object in list position
    '''
    def inner(*args):
        length = len(args)
        if not length:
            return fn()
        else:
            obj = args[-1]
            if _isArray(obj):
                return fn(*args)
            # TODO: see if it's callable
            elif hasattr(obj, methodname) and callable(
                getattr(obj, methodname)
            ):
                getattr(obj, methodname)(*args)
            else:
                # TODO: raise error
                pass
        # Ignoring transducer logic for v1
    return inner
