def sum_of_two_digits(digit1, digit2):
    return digit1 + digit2

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a,b))
