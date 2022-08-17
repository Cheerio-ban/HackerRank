# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum_fast(n):
    arr = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n + 1):
        arr.append(0)
    sum = 1
    for i in range(2, n + 1):
        arr[i] = (arr[i-1] + arr[i-2]) % 10
        sum += arr[i]

    return sum % 10

# print(fibonacci_sum_fast(100))
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))