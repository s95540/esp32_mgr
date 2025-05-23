import gc
import os
import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")
    print("Used heap:", gc.mem_alloc(), "bytes")

def sieve(tab: list[bool], n: int) -> None:
    for i in range(2, int(n**0.5) + 1):
        if not tab[i]:
            for j in range(i * i, n + 1, i):
                tab[j] = True


print_heap("Heap before alg")
n = 10_000
tab = [False] * (n + 1)

start = time.ticks_us()
sieve(tab, n)
end = time.ticks_us()

print_heap("Heap after alg:")

print("Execution time (us):", time.ticks_diff(end, start))
