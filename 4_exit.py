#
# Exit test
# Devina
#

sum = 0

while True:
    x1 = input('Enter x1: ')
    x2 = input('Enter x2: ')
    op = input('Enter operator: ')

    if op == '+':
        sum = int(x1) + int(x2)
    elif op == '-':
        sum = int(x1) - int(x2)

    print(f'Result: {sum}')
    
    option = input('Do you want to continue?')
    if option == 'c':
        continue
    else:
        break
    