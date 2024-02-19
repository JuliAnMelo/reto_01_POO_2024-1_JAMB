number_list = list(map(int, input('Please type a sequence of integers    ').split()))

def maximum_sum(integer_list):
    """
    Mintlify says:
    The `maximum_sum` function takes a list of integers as input and calculates the
    maximum sum of any two consecutive elements in the list. The function iterates through the list and
    compares the sum of each pair of consecutive elements with the current maximum sum, updating it if a
    larger sum is found
    """

    max_sum = 0
    index = 0
    while index < len(integer_list) - 2:
        if integer_list[index] + integer_list[index + 1] > max_sum:
            max_sum = integer_list[index] + integer_list[index + 1]
        index += 1
    return max_sum

print(f'The maximum sum in the list is {maximum_sum(number_list)}')

#is established a variable with a zero value; with a while loop,
#the function add up the integers in the list by pairs,
#updating the value of the variable zero until reaching the end of the list,
#returning the maximum pair sum 