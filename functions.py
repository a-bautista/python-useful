def get_user_input():
    """
        No parameters in this function.

        Prompt the user an integer value for your function. 

        If the value is not an integer, then continue the prompt.

        Return the integer value given by the user.

        Call this docstring with print(get_user_input.__doc__)
    """

    value = input("Enter a numeric value for your function: \n")

    if isinstance(value, str):
        while not value.isnumeric():
            value = input("Enter a numeric value for your function: \n")
    print("You entered a numeric value: "+ str(value))


def main():
    print("Starting")
    
    get_user_input() # 0 arguments in the function

    print("End")

    # print(get_user_input.__doc__)

main()