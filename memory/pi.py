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

def pi_gauss_legendre(n):
    an = 1.0
    bn = 1.0 / math.sqrt(2)
    tn = 0.25
    pn = 1.0

    for _ in range(n):
        update_min_free()
        a_pom = an
        an = (an + bn) / 2
        bn = math.sqrt(a_pom * bn)
        tn -= pn * (a_pom - an) ** 2
        pn *= 2

    return ((an + bn) ** 2) / (4 * tn)

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")
    print("Minimum free heap:", min_free_heap, "bytes")


print_heap("Heap before alg:")

iterations = 25
result = pi_gauss_legendre(iterations)

print_heap("Heap after alg:")
