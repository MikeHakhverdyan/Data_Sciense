def foo(a, b):
    sum = 0
    if a > b:
        a,b = b,a
    while a < b:
        sum += a
        a += 1
    return sum
