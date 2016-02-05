def _take(n, _iter):
    '''
    ramdajs does not include this private function.
    Instead, the private function `_dropLast`
    calls the public `take` method.
    '''
    for i, el in enumerate(_iter):
        if i < n:
            yield el
        else:
            raise StopIteration
