
def display_menu():
    print('''
        Menu Options are:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Exit
    ''')
    option = int(input('Please make a selection: '))
    return option

def continue_working(flag):
    value = input('Do you want to continue working? (y/n) ')
    if value == 'y':
        pass
    elif value == 'n':
        flag = False
    else: 
        flag = True
    return flag

def enter_numbers():
    num1 = get_integer()
    num2 = get_integer()
    return num1, num2

def get_integer():
    num = input('Enter your number: ')
    while not num.isnumeric():
        print('Value must be a numeric value')
        num = input('Enter your first number: ')
    return num

def controller_calculator():
    flag = True
    while flag:
        print('Simple Calculator App')
        option = display_menu()
        if isinstance(option, int):
            if option == 1:
                num1, num2 = enter_numbers()
                sum(num1, num2)
            elif option == 2:
                num1, num2 = enter_numbers()
                subtract(num1, num2)
            elif option == 3:
                num1, num2 = enter_numbers()
                multiply(num1, num2)
            elif option == 4:
                num1, num2 = enter_numbers()
                divide(num1, num2)
            elif option == 5:
                print("Exit completed")
                exit()
            else:
                print("Option not valid, please insert numbers from 1 - 4")
            flag = continue_working(flag)
        else:
            print('Option not valid, please type only one of the numeric values')        
    print("Exit completed")


def sum(a, b):
    print(int(a) + int(b))

def subtract(a, b):
    print(int(a) - int(b))

def multiply(a, b):
    print(int(a) * int(b))

def divide(a, b):
    print(a//b)

def main():
    controller_calculator()

main()