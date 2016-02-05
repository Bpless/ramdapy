def _complement(fn):
    return lambda *args: not fn(*args)
