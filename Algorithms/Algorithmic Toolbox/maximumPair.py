input_numbers = [2, 3, 4, 5, 8, 8, 3]

def max_pairwise_product(input_numbers):
    maximum = 0
    maximum1 = 0
    indexx = 0
    for i in range(len(input_numbers)):
        if input_numbers[i] > maximum:
            maximum = input_numbers[i]
            indexx = i

    for i in range(len(input_numbers)):
        if input_numbers[i] > maximum1 and i != indexx:
            maximum1 = input_numbers[i]

    return maximum1 * maximum
 

# print(max_pairwise_product(input_numbers))

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
