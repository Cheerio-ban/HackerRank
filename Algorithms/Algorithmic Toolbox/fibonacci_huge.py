# Uses python3
from calendar import c
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def pisanoPeriod(m):
        a = 0
        b = 1
        c = a + b
        squared = m * m
        for i in range(squared):
            c = (a + b) % m
            a = b 
            b = c
            if a == 0 and b == 1:
                return i + 1

def get_fibonacci_huge_fast(n, m):
    pisano_period = pisanoPeriod(m)
    n = n % pisano_period
    
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current = current, previous + current
        
    return (current % m)

# print(get_fibonacci_huge_fast(438, 900))

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
