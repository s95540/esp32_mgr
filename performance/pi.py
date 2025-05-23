import time
import math

def pi_gauss_legendre(n):
    an = 1.0
    bn = 1.0 / math.sqrt(2)
    tn = 0.25
    pn = 1.0

    for _ in range(n):
        a_pom = an
        an = (an + bn) / 2
        bn = math.sqrt(a_pom * bn)
        tn -= pn * (a_pom - an) ** 2
        pn *= 2

    return ((an + bn) ** 2) / (4 * tn)

iterations = 25

start = time.ticks_us()
result = pi_gauss_legendre(iterations)
end = time.ticks_us()

print("Execution time (us):", time.ticks_diff(end, start))
