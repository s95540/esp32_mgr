import gc
import os

min_free_heap = gc.mem_free()

def update_min_free():
    global min_free_heap
    gc.collect()
    current_free = gc.mem_free()
    if current_free < min_free_heap:
        min_free_heap = current_free

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")
    print("Minimum free heap:", min_free_heap, "bytes")

def sieve(tab: list[bool], n: int) -> None:
    update_min_free()
    for i in range(2, int(n**0.5) + 1):
        if not tab[i]:
            for j in range(i * i, n + 1, i):
                tab[j] = True
        update_min_free()


print_heap("Heap before alg")

n = 10_000
tab = [False] * (n + 1)
sieve(tab, n)

print_heap("Heap after alg:")
