def pageCount(n, p):
    # Write your code here
    front = p // 2
    back = (n // 2) - (p // 2)
    return min(front, back)
