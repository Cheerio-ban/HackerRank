def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        new = arr[0]
        del arr[0]
        arr.append(new)
    return arr