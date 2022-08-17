# Uses python3
import sys

def get_change(m):
    #write your code here
    numCoins = 0 
    while m > 0:
        if m >= 10:
            m -= 10
        elif 5 <= m < 10:
            m -= 5
        else:
            m -= 1
        numCoins += 1
    return numCoins



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))