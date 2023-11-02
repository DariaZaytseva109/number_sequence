def simple_sequence():
    """Генератор для получения последовательности"""
    n = 1
    while True:
        for _ in range(n):
            yield str(n)
        n += 1


generator = simple_sequence()

for _ in range(int(input())):
    print(next(generator), end='')
