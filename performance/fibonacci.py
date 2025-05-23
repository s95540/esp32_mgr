import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

term = 25

start = time.ticks_us()
result = fibonacci(term)
end = time.ticks_us()

print("Execution time (us):", time.ticks_diff(end, start))
