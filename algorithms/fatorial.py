def fatorial(n):
    if n == 1:
        print(1, end=' = ')
        return 1
    print(n, end=' x ')
    return n * fatorial(n - 1)
