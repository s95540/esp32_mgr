import gc
import time
import os

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")

print_heap("Heap before alg")

term = 25

start = time.ticks_us()
result = fibonacci(term)
end = time.ticks_us()

print_heap("Heap after alg:")

print("Execution time (us):", time.ticks_diff(end, start))
