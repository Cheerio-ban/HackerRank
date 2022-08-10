# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    arr = [0, 1]

    for i in range(2, n+1):
        arr.append((arr[i-1] + arr[i-2]) % 10)
    # print(arr)
    return arr[n]

# print(get_fibonacci_last_digit_fast(327305))


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))