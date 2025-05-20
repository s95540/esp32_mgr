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

def main():
    n = 10_000
    tab = [False] * (n + 1)

    print_heap("Heap before alg")

    start = time.ticks_us()
    sieve(tab, n)
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
