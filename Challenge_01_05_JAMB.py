some_strings = list(map(str, input('Please type a list of words    ').split()))

def words_with_the_same_letters(strings):
    """
    Mintlify says:
    The function `words_with_the_same_letters` takes a list of strings as input, sorts the
    strings by length, converts each string into a set of characters, and then checks for strings that
    have the same set of characters. It returns a string containing the strings that have the same set
    of characters.
    """

    string_list = sorted(strings, key = len)
    string_set = []
    for a_string in string_list:
        string_set.append(set(a_string))

    equal_sets = set()
    index_one = 0
    while index_one < (len(string_set) - 1):
        index_two = index_one + 1
        while index_two < len(string_set):
            if string_set[index_one] != string_set[index_two]:
                index_two += 1
            else: 
                equal_sets.add(string_list[index_one])
                equal_sets.add(string_list[index_two])
                index_two += 1
        index_one += 1

    return ', '.join(map(str, equal_sets))

iwanttosleep = words_with_the_same_letters(some_strings)

if len(iwanttosleep) > 0:
    print(f'The words with the same letters are: {iwanttosleep}')
if len(iwanttosleep) == 0:
    print('There aren\'t any words with the same letters.')

#This thing compares the word given by the user as sets,
#doing one loop in other one with two index variables at the same time,
#it works assuming that is only one set of letter repeated