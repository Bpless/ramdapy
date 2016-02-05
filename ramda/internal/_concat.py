import itertools


def _concat(a, b):
    '''
        Private `concat` function to merge two array-like objects.

        ramda.js does not curry this function.  In large part,
        that appears due to the fact that the @public `concat`
        method does not alias to this func.  Instead,
        it uses invocation to delegate to object concat methods.
        That invocation does not make sense here, as
        concat-able objects should export an __iter__ interface.

            @private
            @param {Array|Arguments} [set1=[]] An array-like object.
            @param {Array|Arguments} [set2=[]] An array-like object.
            @return {Array} A new, merged array.
            @example
              _concat([4, 5, 6], [1, 2, 3]); //=> [4, 5, 6, 1, 2, 3]
    '''
    return [i for i in itertools.chain(a, b)]
