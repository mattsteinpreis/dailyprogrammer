def reverse_factorial(n, i=1):
    next = n / i
    if next == 1:
        return i
    if next < 1:
        return None
    return reverse_factorial(next, i+1)

input_list = [3628800, 479001600, 6, 18]
for number in input_list:
    rf = reverse_factorial(number)
    if rf:
        print(number, ' = ', rf, '!', sep='')
    else:
        print(number, 'NONE', sep=' ')