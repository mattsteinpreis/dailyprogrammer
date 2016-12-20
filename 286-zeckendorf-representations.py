def build_fibs(max=1000):
    f = [1,2]
    while f[-1] <= max:
        f.append(sum(f[-2:]))
    return f[:-1]


def zeckrep(target):
    fibs = build_fibs(target)
    total = 0
    used = []
    for fi in fibs[::-1]:
        if total + fi > target:
            continue
        used.append(fi)
        total += fi
        if total == target:
            print(' '.join([str(target),
                            '=',
                            ' + '.join([str(d) for d in used])]))
            return


if __name__ == '__main__':
    n_cases = int(input())
    cases = []
    for i in range(n_cases):
        t = int(input())
        zeckrep(t)