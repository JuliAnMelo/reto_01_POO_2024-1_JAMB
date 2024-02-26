def words_with_the_same_letters(strings):
    """
    Mintlify says:
    The function `words_with_the_same_letters` takes a list of strings as input, sorts the
    strings by order as lists, and then checks for lists that
    have the same characters. It returns a string containing the strings that have the same letters.
    """

    anagram_strings = []
    index_one = 0
    while index_one < (len(string_list) - 1):
        index_two = index_one + 1
        while index_two < len(string_list):
            if sorted(list(string_list[index_one])) != sorted(list(string_list[index_two])):
                index_two += 1
            else:
                if string_list[index_one] not in anagram_strings: anagram_strings.append(string_list[index_one])
                if string_list[index_two] not in anagram_strings: anagram_strings.append(string_list[index_two])
                index_two += 1
        index_one += 1

    return ', '.join(anagram_strings)

#This thing compares the word given by the user as sets,
#doing one loop in other one with two index variables at the same time,
#it works assuming that is only one set of letter repeated

if __name__ == "__main__": 
    SOME_STRINGS = list(map(str, input('Please type a list of words    ').split()))
    iwanttosleep = words_with_the_same_letters(SOME_STRINGS)
    if len(iwanttosleep) > 0:
        print(f'The words with the same letters are: {iwanttosleep}')
    if len(iwanttosleep) == 0:
        print('There aren\'t any words with the same letters.')
