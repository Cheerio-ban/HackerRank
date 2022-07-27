def reverseArray(a):
    # Write your code here
    i = 0
    j = len(a) - 1
    while i < j:
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        i += 1
        j -= 1
    return a