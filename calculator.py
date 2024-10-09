num_1: float = float(input('Enter first number: '))
num_2: float = float(input('Enter second number: '))
operator: str = input('Enter operation symbol(+ , - , * , / , ** , // , % ): ')
if operator == '+':
    sum = num_1 + num_2
    print(sum)
elif operator == '-':
    sum = num_1 - num_2
    print(sum)
elif operator == '*':
    sum = num_1 * num_2
    print(sum)
elif operator == '/':
    sum = num_1 / num_2
    print(sum)
elif operator == '**':
    sum = num_1 ** num_2
    print(sum)
elif operator == '//':
    sum = num_1 // num_2
    print(sum)
elif operator == '%':
    sum = num_1 % num_2
    print(sum)
else:
    print('Please input one operator from the given list')