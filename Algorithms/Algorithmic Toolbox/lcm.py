# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    current_gcd = a
    return current_gcd

def lcm_fast(a, b):
    gcd = gcd_fast(a, b)
    lcm = (a * b) // gcd
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))