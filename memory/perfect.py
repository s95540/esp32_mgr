import gc
import os
import math

min_free_heap = gc.mem_free()

def update_min_free():
    global min_free_heap
    gc.collect()
    current_free = gc.mem_free()
    if current_free < min_free_heap:
        min_free_heap = current_free

def is_perfect(n):
    update_min_free()
    s = 1
    p = int(math.sqrt(n))
    for i in range(2, p + 1):
        update_min_free()
        if n % i == 0:
            s += i + n // i
    if p * p == n:
        s -= p
    update_min_free()
    return n == s

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")
    print("Minimum free heap:", min_free_heap, "bytes")


print_heap("Heap before alg:")

a = 9223372
result = is_perfect(a)

print_heap("Heap after alg:")
