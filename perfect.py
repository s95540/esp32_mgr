import gc
import os
import time
import math

def is_perfect(n):
    s = 1
    p = int(math.sqrt(n))
    for i in range(2, p + 1):
        if n % i == 0:
            s += i + n // i
    if p * p == n:
        s -= p
    return n == s

def print_heap(label):
    gc.collect()
    print(label)
    print("Free heap:", gc.mem_free(), "bytes")
    print("Used heap:", gc.mem_alloc(), "bytes")

def main():
    a = 92233

    print_heap("Heap before alg:")

    start = time.ticks_us()

    result = is_perfect(a)

    end = time.ticks_us()

    print_heap("Heap after alg:")

    print("Execution time (us):", time.ticks_diff(end, start))

    fs_stat = os.statvfs('/')
    block_size = fs_stat[0]
    total_blocks = fs_stat[2]
    free_blocks = fs_stat[3]

    total_space = block_size * total_blocks
    free_space = block_size * free_blocks

    print("Total filesystem size:", total_space, "bytes")
    print("Free filesystem space:", free_space, "bytes")

main()
