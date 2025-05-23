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

a = 9223372

start = time.ticks_us()
result = is_perfect(a)
end = time.ticks_us()

print("Execution time (us):", time.ticks_diff(end, start))
