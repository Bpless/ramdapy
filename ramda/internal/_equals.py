def _equals(a, b):
    '''
    The large operating assumption here is that == performs
    a sufficient deep equality check in Python.  This
    greatly simplifies the logic, compared to ramda js.

    The latter has many checks for Type and value
    specific edge cases.
    '''
    return a == b
