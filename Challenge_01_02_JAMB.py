def palindrome(wrd):
    """
    Mintlify says:
    The function checks if a given word is a palindrome.
    """

    wrds = list(wrd)
    pal = True
    while len(wrds) > 1 and pal == True:
        if wrds[0] == wrds[-1]:
            del wrds[0]
            del wrds[-1]
        else:
            pal = False       
    if pal == False: return 'is not'
    else: return 'is'

#I thought about converting the input in a list,
#and through a while loop compare and eliminate the first and last letter
#to verify if the word is a palindrome

if __name__ == "__main__": 
    WORD = input('Please write a word:    ')
    print(f'The word \'{WORD}\' {palindrome(WORD)} a palindrome')
