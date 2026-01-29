import time

def fib_binet_exact(n: int) -> int:
    """Compute Fibonacci number using algebra in Z[√5]."""
    class Zrt5:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __mul__(self, other):
            return Zrt5(self.a * other.a + 5 * self.b * other.b,
                        self.a * other.b + self.b * other.a)
        def half(self):
            return Zrt5(self.a // 2, self.b // 2)

    if n == 0:
        return 0
    step = Zrt5(1, 1)
    fib = Zrt5(1, 1)
    n -= 1
    while n > 0:
        if n & 1:
            fib = (fib * step).half()
        step = (step * step).half()
        n >>= 1
    return fib.b


def benchmark_one_second():
    start = time.time()
    n = 0
    last_fib = 0
    while time.time() - start < 1.0:  # run for 1 second
        last_fib = fib_binet_exact(n)
        n += 1
    print(f"Reached F({n-1}) in ~1 second")
    print(f"F({n-1}) has {len(str(last_fib))} digits")
    print(f"F({n-1}) = {last_fib}")

benchmark_one_second()
