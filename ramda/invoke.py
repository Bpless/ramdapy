from ramda.internal._curry2 import _curry2
from ramda.internal._curryN import _curryN


@_curry2
def invoke(arity, method):
    '''
    Turns a named method with a specified arity into a function that can be
    called directly supplied with arguments and a target object.

    The returned function is curried and accepts `arity + 1` parameters where
    the final parameter is the target object.

        @func
        @memberOf R
        @since v0.1.0
        @category Function
        @sig Number -> String -> (a -> b -> ... -> n -> Object -> *)
        @param {Number} arity Number of arguments the returned function
                        should take before the target object.
        @param {String} method Name of the method to call.
        @return {Function} A new curried function.
        @example
            fetch = R.invoker(1, 'fetch');
            fetch('stick', dog); // some value

            fetch_location = R.invoker(2, 'fetch_location')('yard');
            fetch_location('stick', dog); // some value
    '''

    def inner(*args):
        target = args[arity]
        can_invoke = all([
            target is not None,
            hasattr(target, method),
            callable(getattr(target, method))
        ])
        if can_invoke:
            return getattr(target, method)(*args[:arity])
        else:
            raise TypeError(
                '{} does not have a {} method'.format(target, method)
            )
    return _curryN(arity + 1, inner)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def fetch(self, location, thing):
        return self.name + location + thing

dog = Dog('tom')

fetch = invoke(2, 'fetch')
print fetch('backyard', 'stick', dog)

