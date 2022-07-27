def sockMerchant(n, ar):
    # Write your code here
    hashMap = {}
    count = 0
    for elem in ar:
        if elem in hashMap:
            hashMap[elem] += 1
            if hashMap[elem] == 1:
                count += 1
                del hashMap[elem]
        else:
            hashMap[elem] = 0
    return count
