# Reto 01 Programación Orientada a Objetos Julian Melo

# Ejercicio 01

La función toma dos operandos y un operador como una lista, retornando el resultado de su operación, teniendo en cuenta ciertas caracteristicas de la división:

```python

def calculator(two_variables_one_operator_list):
   
    num1, num2, = int(two_variables_one_operator_list[0]), int(two_variables_one_operator_list[1])
    operator = two_variables_one_operator_list[2]
    if operator == '+': return num1 + num2, 'plus'
    if operator == '-': return num1 - num2, 'minus'
    if operator == '*': return num1 * num2, 'times'
    if operator == '/':
        if num2 == 0: return 'invalid', 'divided'
        if num1 % num2 != 0: return num1 / num2, 'divided'
        else: return num1 // num2, 'divided'

if __name__ == "__main__": 
    USER_INPUT = list(input('Please write two integers and an operator    ').split())
    print(f'The result of {USER_INPUT[0]} {calculator(USER_INPUT)[1]} {USER_INPUT[1]} is {calculator(USER_INPUT)[0]}')

```

# Ejercicio 02

La función toma la palabra como una lista de caracteres, comparando el primero con el último, el segundo con el penúltimo, etcetera, retornando sí es o no palíndroma:

```python

def palindrome(wrd):

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

if __name__ == "__main__": 
    WORD = input('Please write a word:    ')
    print(f'The word \'{WORD}\' {palindrome(WORD)} a palindrome')

```

# Ejercicio 03

La función, de hecho, busca los números que no son primos, añadiendolos a un conjunto, así pues al terminar el ciclo for, compara este conjunto con el conjunto de los números dados por el usuario, retornando el conjunto de la diferencia como una cadena, es decir, los números primos:

```python

def prime_hunter(integer_list):

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

if __name__ == "__main__": 
    NUMBER_LIST = list(map(int, input('Please type a sequence of integers    ').split()))
    pleasework = prime_hunter(NUMBER_LIST)
    if len(pleasework) > 0:
        print(f'The prime numbers in the given list are: {pleasework}')
    if len(pleasework) == 0:
        print('There aren\'t any prime numbers in the list.')

```

# Ejercicio 04

Estableciendo una variable con valor de la suma de los dos primeros items de la lista dada, mediante un ciclo while, la función compara la suma de los items consecutivos, retornando la de mayor valor: 

```python

def maximum_sum(integer_list):

    max_sum = integer_list[0] + integer_list[1]
    index = 0
    while index < len(integer_list) - 1:
        if integer_list[index] + integer_list[index + 1] > max_sum:
            max_sum = integer_list[index] + integer_list[index + 1]
        index += 1
    return max_sum

if __name__ == "__main__": 
    NUMBER_LIST = list(map(int, input('Please type a sequence of integers    ').split()))
    print(f'The maximum sum in the list is {maximum_sum(NUMBER_LIST)}')

```

# Ejercicio 05

La función toma la lista de palabras dada, mediante un ciclo while, y dos variables de índice, compara las palabras convertidad en listas ordenadas alfabeticamente, agregandolas o no a una lista que será el retorno, la lista de palabras de la misma longitud que contienen las mismas letras:

```python

def words_with_the_same_letters(string_list):

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

if __name__ == "__main__": 
    SOME_STRINGS = list(map(str, input('Please type a list of words    ').split()))
    iwanttosleep = words_with_the_same_letters(SOME_STRINGS)
    if len(iwanttosleep) > 0:
        print(f'The words with the same letters are: {iwanttosleep}')
    if len(iwanttosleep) == 0:
        print('There aren\'t any words with the same letters.')
