def circularArrayRotation(a, k, queries):
    # Write your code here
    result = []
    for i in range(k):
        new = a.pop()
        a.insert(0, new)
    for i in range(len(queries)):
        result.append(a[queries[i]])
        
    return result