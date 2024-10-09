# Starting variable name should not have number
# 10 is integer
# 'hello' is string
# True or False is boolean
# 10.5 is decimal 
# num: int = 10 is to indicate this is a int
#name: str = input('Enter name: ')
#print(f'The name is {name}')
number1 = float(input('Enter number: '))
number2 = float(input('Enter number: '))
if number1 == number2:
    print('Both are same')
elif number1 > number2:
    print('First number is greater than second number')
elif number1 < number2:
    print('Second number is greater than first number')
else:
    print('Both are different')