USER_INPUT = list(input('Please write two integers and an operator    ').split())

def calculator(two_variables_one_operator_list):
    """
    Mintlify says:
    The function `calculator` takes a list of two variables and one operator, performs the corresponding
    arithmetic operation, and returns the result along with a string indicating the operation performed.
    """
   
    num1, num2, = int(two_variables_one_operator_list[0]), int(two_variables_one_operator_list[1])
    operator = two_variables_one_operator_list[2]
    if operator == '+': return num1 + num2, 'plus'
    if operator == '-': return num1 - num2, 'minus'
    if operator == '*': return num1 * num2, 'times'
    if operator == '/':
        if num2 == 0: return 'invalid', 'divided'
        if num1 % num2 != 0: return num1 / num2, 'divided'
        else: return num1 // num2, 'divided'

print(f'The result of {USER_INPUT[0]} {calculator(USER_INPUT)[1]} {USER_INPUT[1]} is {calculator(USER_INPUT)[0]}')

#It takes the integers and the operator as a list, 
#the function simply does the input asigned operation 
