#Build a Calculator that takes inputs from the user and a specific operator and calculates the correct value.
# Example: 2 + 5 = 7, 5 * 5 = 25, 8 / 4 = 2

#Build Inputs for the user to enter in the information.

firstNum = input('Please enter in the first number:  ')
userOperator = input('Please enter in your operator (Add, Subtract, Multiply, Divide): ')
secondNum = input('Please enter in the second number: ')

#Build a group of If Else Statements, convert the inputs to integers, and returns the correct values.

if userOperator == '+':
    calc = int(firstNum) + int(secondNum)

elif userOperator == '-':
    calc = int(firstNum) - int(secondNum)

elif userOperator == '*':
    calc = int(firstNum) * int(secondNum)

elif userOperator == '/':
    calc = int(firstNum) / int(secondNum)

else: 
    print('You have entered an invalid operator!')

print(calc)

#testing git