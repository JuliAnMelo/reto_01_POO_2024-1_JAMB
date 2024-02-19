NUMBER_LIST = list(map(int, input('Please type a sequence of integers    ').split()))

def prime_hunter(integer_list):
    """
    Mintlify says:
    The `prime_hunter` function takes a list of integers as input and aims to find
    the prime numbers within that list. The function first sorts the list in descending order and then
    iterates through each integer to determine if it is a prime number
    :return: The `prime_hunter` function is returning a string that contains all the prime numbers from
    the input `integer_list`.
    """

    integer_list.sort(reverse=True)
    no_prime_numbers = {0, 1}
    for integer in integer_list:
        if integer > 2: 
            if integer % 2 == 0: no_prime_numbers.add(integer)
            else:
                divider = 3
                while divider < (integer / 2):
                    if integer % divider == 0: 
                        no_prime_numbers.add(integer)
                        break
                    else: divider += 2     
    prime_numbers = list((set(NUMBER_LIST) - no_prime_numbers))
    return ', '.join(map(str, prime_numbers))

pleasework = prime_hunter(NUMBER_LIST)

if len(pleasework) > 0:
    print(f'The prime numbers in the given list are: {pleasework}')
if len(pleasework) == 0:
    print('There aren\'t any prime numbers in the list.')

#This one may be mot the most efficent form to do this challenge,
#but it takes the list of integers in descendent order searching for
#the numbers that are NOT prime and putting them in a set that contains
#number one and number zero, finally, it get the prime numbers comparing
#the initial list in form of a set, returning the list of prime numbers
#as a string   