def _pipe(f, g):
    return lambda *args: g(f(*args))
