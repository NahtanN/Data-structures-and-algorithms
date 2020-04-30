def fibonacci_generator(val):
    p = 0
    s = 1
    while s < val:
        yield s
        p, s = s, p + s

print([x for x in fibonacci_generator(50)])
