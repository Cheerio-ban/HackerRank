# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)

#Memoization
def calc_fib_fast(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    # print(arr)
    return arr[n]


# print(calc_fib_fast(3))

if __name__ == '__main__':
    n = int(input())
    # print(calc_fib(n))
    print(calc_fib_fast(n))