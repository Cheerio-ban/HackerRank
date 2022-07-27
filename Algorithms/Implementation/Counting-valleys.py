def countingValleys(steps, path):
    # Write your code here
    seaLevel = 0
    valley = 0
    for i in range(len(path)):
        if path[i] == 'D':
            if seaLevel == 0:
                valley += 1
                seaLevel -= 1
            else:
                seaLevel -= 1
        elif path[i] == 'U':
            seaLevel += 1
    return valley