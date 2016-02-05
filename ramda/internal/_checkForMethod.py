def _checkForMethod(methodname, fn):
    '''
    Similar to `hasMethod`, this checks whether a function has a
    [methodnamefunction]. If it isn't an array it will execute
    that function otherwise it will defer to ramda.

    _checkForMethod is utilized by functions that operate on arrays
    generally (i.e. forEach, tail, etc).

    Here, we are extending the is_array check to include lists and tuples.
    This method seems generally less intuitive in ramda.js and even
    more so in its translation to Python.

    implementation
      @private
      @param {Function} fn ramda implemtatio
      @param {String} methodname property to check for a custom implementation
      @return {Object} Whatever the return value of the method is
    '''
    def inner(*args):
        if (len(args) == 0):
            return fn()
        else:
            obj = args[-1]
            is_implemented = (
                hasattr(obj, methodname) and callable(getattr(obj, methodname))
            )
            is_array = isinstance(obj, list) or isinstance(obj, tuple)
            if is_array(obj) or not is_implemented:
                return fn(*args)
            else:
                return getattr(obj, methodname)(*args[:-1])
    return inner
