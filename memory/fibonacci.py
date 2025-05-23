import gc
import os

min_free_heap = gc.mem_free()

def update_min_free():
    global min_free_heap
    # gc.collect()
    current_free = gc.mem_free()
    if current_free < min_free_heap:
        min_free_heap = current_free

def fibonacci(n):
    update_min_free()
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")
    print("Minimum free heap:", min_free_heap, "bytes")


print_heap("Heap before alg")

term = 25
result = fibonacci(term)

print_heap("Heap after alg:")
