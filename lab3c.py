#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: rsharma346(117061226)

def operate(number1, number2, operator):
    # Use conditional logic to handle different operations
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))       # Should return 15
    print(operate(10, 5, 'subtract'))  # Should return 5
    print(operate(10, 5, 'multiply'))  # Should return 50
    print(operate(10, 5, 'divide'))    # Should return error message

