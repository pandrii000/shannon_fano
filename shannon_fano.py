from collections import Counter


def encode(X, P, indices, code):
    if len(indices) < 2:
        return

    li = 0
    ri = len(indices) - 1

    lsum = P[indices[li]]
    rsum = P[indices[ri]]

    while li + 1 < ri:
        if lsum <= rsum:
            li += 1
            lsum += P[indices[li]]
        else:
            ri -= 1
            rsum += P[indices[ri]]

    mid = ri
    l = indices[:mid]
    r = indices[mid:]

    for i in l:
        code[i] += '0'

    for i in r:
        code[i] += '1'

    encode(X, P, l, code)
    encode(X, P, r, code)


def encode_text(text):
    d = Counter()
    s = 0
    for c in text:
        d[c] += 1
        s += 1

    probabilities = {k: v / s for k, v in d.items()}
    X, P = map(tuple, zip(*probabilities.items()))

    n = len(X)
    code = [''] * n

    P, indices = zip(*sorted(zip(P, range(n))))
    X = [X[i] for i in indices]

    encode(X, P, list(range(n)), code)
    return X, P, code


if __name__ == '__main__':
    text = 'AAAbbbcc'
    X, P, code = encode_text(text)
    print('{:<10} {:<15} {:<10}'.format('Symbol', 'Probability', 'Code'))
    for symbol, probability, c in zip(X, P, code):
        print('{:<10} {:<15} {:<10}'.format(symbol, '%.3f' % probability, c))
