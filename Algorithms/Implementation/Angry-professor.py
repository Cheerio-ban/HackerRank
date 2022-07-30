def angryProfessor(k, a):
    # Write your code here
    count = 0
    for elem in a:
        if elem <= 0:
            count += 1
    if count < k:
        return "YES"
    return "NO"