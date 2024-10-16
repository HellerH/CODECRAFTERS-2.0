import sys

try:
  num_1: float = float(input('Enter first number: '))
except ValueError:
    print('Please input a valid number')
    print('Please rerun program')
    sys.exit()
except NameError:
    print('Please rerun program')
try:
   num_2: float = float(input('Enter second number: '))
except ValueError:
    print('Please input a valid number')
    print('Please rerun program')
    sys.exit()
except NameError:
    print('Please rerun program')


operator: str = input('Enter operation symbol(+ , - , * , / , ** , // , % ): ')


if operator == '+':
    try:
       sum = num_1 + num_2
       print(f'Your result is {sum}')
    except NameError:
        print('Please rerun program')
elif operator == '-':
    try:
       sum = num_1 - num_2
       print(f'Your result is {sum}')
    except NameError:
        print('Please rerun program')
elif operator == '*':
    try:
       sum = num_1 * num_2
       print(f'Your result is {sum}')
    except NameError:
        print('Please rerun program')
elif operator == '/':
    try:
       sum = num_1 / num_2
       print(f'Your result is {sum}')
    except ZeroDivisionError:
        print('Division by zero not possible')
    except NameError:
        print('Please rerun program')
elif operator == '**':
    try:
       sum = num_1 ** num_2
       print(f'Your result is {sum}')
    except NameError:
        print('Please rerun program')
elif operator == '//':
    try:
      sum = num_1 // num_2
      print(f'Your result is {sum}')
    except ZeroDivisionError:
        print('Division by zero not possible')
    except NameError:
        print('Please rerun program')
elif operator == '%':
    try:
       sum = num_1 % num_2
       print(f'Your result is {sum}')
    except ZeroDivisionError:
        print('Remainder not defined')
    except NameError:
        print('Please rerun program')
else:
    print('Please input one operator from the given list')