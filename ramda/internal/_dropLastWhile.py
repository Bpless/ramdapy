def _dropLastWhile(pred, _iter):
    xs = list(_iter)
    idx = len(xs) - 1
    while (idx >= 0 and pred(xs[idx])):
        idx -= 1

    return xs[0: idx + 1]
