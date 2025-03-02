expenses = []

quit = False

while not quit:
    print('\nMain menu: ')
    print('1. Add expenses ')
    print('2. Calculate sum of all expenses ')
    print('3. Quit')

    choice = int(input('Your choice: '))

    if choice == 1:
        amount = float(input('Write a sum of expense: '))
        expenses.append(amount)
        print('Expense has been added.')
    elif choice == 2:
        total = sum(expenses)
        print(f'The total expenses is {total} EUR.')
    elif choice == 3:
        print('Bye! See you soon!')
        quit = True
    else:
        print('Wrong option!')